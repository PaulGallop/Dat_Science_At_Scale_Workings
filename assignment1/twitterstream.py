import oauth2 as oauth
import urllib2 as urllib

# See assignment1.html instructions or README for how to get these credentials

# NOTE Stop stream by using interupt AND then delete last line of text file
# which is likely to be incomplete or malformed

api_key = "T2jZ7jM4HKhMpEAIe9Ouj82ZD"
api_secret = "QZdkucNKWRSZDeaeMqDt2VmLRddhPnKpj0sqmPZkNXhlQXFsC8"
access_token_key = "216475513-cX7b06ohDHC2uLoRIsOJ1vHxmevyzAD78b5ExupY"
access_token_secret = "7YN0YYlQl0SARomm6XNS33ivnepiMfx5RuEnMqJUtuQC5"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()
  
  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)
  return response

def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  
  f = open('output.txt', 'w') ## sets up output file. WARNING WILL OVERWRITE

  for line in response:
    f.write(line.strip())
    f.write("\n")
  f.close()

if __name__ == '__main__':
  fetchsamples()
