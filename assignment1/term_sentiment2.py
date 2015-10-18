## Data Science at Scale Week 1 Problem 3

## Derive the sentiment of new words based on the sentiment of the tweet

import sys
import json

def main():
    ## afinnfile = open(sys.argv[1])
    ## tweet_file = sys.argv[2]
    
    afinnfile = open("AFINN-111.txt")
    tweet_file = raw_input ("Enter tweet source file: ")
    
    ## Create a data structure for sentiment scores of new words newsent
    newsentiment = dict()
    newcount = dict()
    score = float()
    
    ## Unpack the contents of the sentament file into a dictionary - scores
    ## with each pair being a word/score
    
    scores = dict()
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    afinnfile.close()

    ## Calculate sentiment for each tweet and then use this to build up an estimate
    ## of the sentiment of words not in the original sentiment file
    
    with open(tweet_file, "r") as tweets:
        
        ## Work through the tweet file line by line
        for line in tweets:
            
            jsonline = dict()
            sentiment = 0
            
            ## Parse each line of JSON and extract the text field
            jason_string = line.rstrip() ## removes CRs etc...
            jsonline = json.loads(jason_string)
            if "text" in jsonline:
                text = jsonline["text"]
            else:
                text = ""
            
            ## Calculate sentiment score for this line's text
            words = text.split()
            for word in words:
                if not word in scores: continue
                sentiment = sentiment + scores[word]

            ## Use this sentiment score for the line to create scores for new words
            if text == "": continue ## May also need to add exception handling for non-english text?
            for word in words:
                if word not in newsentiment:
                    newsentiment[word] = sentiment
                    newcount[word] = 1
                else:
                    score = newsentiment[word] + sentiment
                    newsentiment[word] = score
                    newcount[word] = newcount[word] + 1
                
    ## When all tweet have been examined normalise the new word sentiment estimates
    ## and print to std out
    
    for word in newsentiment:
        newsentiment[word] = newsentiment[word] / newcount[word]
        print word, newsentiment[word]
  
if __name__ == '__main__':
    main()
