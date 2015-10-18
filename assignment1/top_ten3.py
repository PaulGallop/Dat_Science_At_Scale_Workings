## Data Science at Scale Week 1 Problem 6

## Computes the ten most frequently occurring hashtags from the data gathered in Problem 1.

import sys
import json

def main():
    ## tweet_file = sys.argv[1]

    tweet_file = "hashtageg.txt"

    hashcount = dict()
    
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
            else:
                hashtags.clear() 

            ## Increment counts of hashtags
            for hashtag in hashtags:
                if hashtag not in hashcount:
                    hashcount[hashtag] = 1
                else:
                    hashcount[hashtag] = hashcount[hashtag] + 1
                
    for hashtag in hashcount:
        print hashtag, hashcount[hashtag]  
                 
if __name__ == '__main__':
    main()
