## Data Science at Scale Week 1 Problem 2

## Derive the sentiment of each tweet

## For this part, you will compute the sentiment of each tweet based on the 
## sentiment scores of the terms in the tweet. The sentiment of a tweet is 
## equivalent to the sum of the sentiment scores for each term in the tweet.

import sys
import json

def main():
    ## afinnfile = open(sys.argv[1]) ## Commented out command line parameter input
    ## tweet_file = open(sys.argv[2]) ## Commented out command line parameter input
    
    afinnfile = open("AFINN-111.txt") ## Delete to revert to command line parameter input
    tweet_file = raw_input ("Enter source file: ") ## Delete to revert to command line parameter input
    ## tweet_file = open("problem_1_submission.txt") ## Delete to revert to command line parameter input
    
    ## Unpack the contents of the sentament file into a dictionary - scores
    ## with each pair being a word/score
    scores = dict()
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    afinnfile.close()

    ## step through the tweet responses line by line, converting them from json
    ## to a dictionary jsonline (note this is over writen for each line), and
    ## then applying a sentiment score for each tweet (line) and write to file

    sf = open ("sentiment.txt", "w") ## results file

    with open(tweet_file, "r") as tweets: ## handles opening, closing & memory management
        for line in tweets:
            jsonline = dict()
            jason_string = line.rstrip() ## removes CRs etc...
            jsonline = json.loads(jason_string)
            text = jsonline["text"]
            print text
            
            ## calculate sentiment score for this line and write to file
            words = text.split()
            print words
            sentiment = 0
            for word in words:
                sentiment = sentiment + scores[word] ## need some error handling if word isn't a term

            sf.write(sentiment)
            sf.write("\n")
            
    sf.close()      

    
if __name__ == '__main__':
    main()



