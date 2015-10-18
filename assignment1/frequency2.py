## Data Science at Scale Week 1 Problem 4

## Computes the term frequency histogram of the livestream data harvested for 
## Problem 1.The frequency of a term can be calculated as 
## [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]

import sys
import json

def main():
    ## tweet_file = sys.argv[1]

    tweet_file = raw_input ("Enter tweet source file: ")

    wordcount = dict()
    totalwords = float()
    frequency = float()
    
    with open(tweet_file, "r") as tweets:
        
        ## Work through the tweet file line by line
        for line in tweets:
            
            jsonline = dict()
            
            ## Parse each line of JSON and extract the text field
            jason_string = line.rstrip() ## removes CRs etc...
            jsonline = json.loads(jason_string)
            if "text" in jsonline:
                text = jsonline["text"]
            else:
                text = ""
            
            ## Extract the text into a list of words
            words = text.split()
            totalwords = totalwords + len(words)

            ## Increment counts of words
            for word in words:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] = wordcount[word] + 1
                
    ## Calculate frequency of each word seem and print
    for word in wordcount:
        frequency = wordcount[word]/totalwords
        print word, frequency
  
if __name__ == '__main__':
    main()
