## Data Science at Scale Week 1 Problem 6

## Computes the ten most frequently occurring hashtags from the data gathered in Problem 1.

import sys
import json

def main():
    ## tweet_file = sys.argv[1]

    tweet_file = "problem_1_submission.txt"
    
    hashcount = dict()
    hashlist = dict()
    
    with open(tweet_file, "r") as tweets:
        
        ## Work through the tweet file line by line
        for line in tweets:
                
            jsonline = dict()
            entities = dict()
                    
            ## Parse each line of JSON and extract the entities (a dictionary) and 
            ## then the hashtags from it. Hashtags are a list of hashtags with each
            ## hashtag a dictionary of which we are interested in "text"
                    
            jason_string = line.rstrip() ## removes CRs etc...
            jsonline = json.loads(jason_string)
            if "entities" in jsonline:
                entities = jsonline["entities"]
                print "ENTITIES >>>>>> ", entities
                hashtags = entities["hashtags"]
                print "HASHTAGS >>>>>> ", hashtags
                
                # Extract the text of each hashtag and print
                index = 0
                while index < len(hashtags):
                    hashtag = hashtags[index]
                    hashtext = hashtag["text"]
                    print hashtext
    
                    ## Increment counts of hashtags
                    if hashtext not in hashlist:
                        hashcount[hashtext] = 1
                        hashlist[hashtext] = hashtext
                    else:
                        hashcount[hashtext] = hashcount[hashtext] + 1
                    
                    index = index + 1
                    
    # Print out list of hashes and frequencies
    for hash in hashlist:
        print hashlist[hash], hashcount[hash]
        
if __name__ == '__main__':
    main()
