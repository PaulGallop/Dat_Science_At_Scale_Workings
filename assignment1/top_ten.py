## Data Science at Scale Week 1 Problem 6

## Computes the ten most frequently occurring hashtags from the data gathered in Problem 1.

import sys
import json
import operator

def main():
    tweet_file = sys.argv[1]
    ## tweet_file = "output.txt"
    
    hashcount = dict()
    frequency = float()
    
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
                hashtags = entities["hashtags"] # maybe there is a way of accessing this in one line?
                
                # Extract the text of each hashtag
                index = 0
                while index < len(hashtags):
                    hashtag = hashtags[index]
                    hashtext = hashtag["text"]
    
                    ## Increment counts of hashtags
                    if hashtext not in hashcount:
                        hashcount[hashtext] = 1
                    else:
                        hashcount[hashtext] = hashcount[hashtext] + 1
                    
                    index = index + 1
    
    # Sort list of hashtags by frequency
    # dict.items() returns a list of 2-tuples ([(key, value), (key, value), ...]),
    # which can the be sorted (a dictionary can't be sorted
    sorted_hashcount = sorted(hashcount.items(), key=operator.itemgetter(1), reverse=True)
    index = 0
    
    # Print out top 10 hashtags and their frequencies
    while index < 10:
        text, frequency = sorted_hashcount[index] # assigns the two elements in tuple[index]
        print text, frequency
        index = index + 1

if __name__ == '__main__':
    main()
