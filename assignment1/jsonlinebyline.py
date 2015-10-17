## Experiments with json reader

import json
import os

def lbl(fn):
    
    # simple parse of 1st line
    
    f = open(fn, "r")
    line = f.readline()
    jason_string = line.strip()
    print jason_string
    data = json.loads(jason_string)
    print "here is the parsed data>>>"
    print data

def manyl(fn):
    
    # parse multiple lines ... works for the 2 lines on output 6
    count = 0
    data = dict()
    with open(fn, "r") as f: ## handles opening, closing & memory management
        for line in f:
            count = count + 1
            jason_string = line.rstrip() ## removes CRs etc...
            data = json.loads(jason_string)
            
    print data
    
def manyl2(fn, noslines):
    
    # parse multiple lines ... DOES NOT WORK for the 2 lines on output 6
    count = 0
    f = open(fn, "r")
    while count < (noslines + 1):
        count = count + 1
        line = f.readline()
        jason_string = line.strip()
        print count
        data = json.loads(jason_string)
    print "here is the parsed data>>>"
    print data
    fn.close()

filename = raw_input("enter a file name: ")
manyl(filename)