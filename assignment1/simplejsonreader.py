## Experiments with json reader

import json

## Parsing json strings

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(json_string) # parsed_json can now be used as a normal dictionary

# EG
print(parsed_json['first_name'])

## Parsing json from a file PART 1

# Create a test file with the same content as the string example
f = open ("jsontest.json", "w")
f.write(json_string.encode('utf-8'))
f.close()

f = open ("jsontest.json", "r")
data = json.load(f)
f.close()

print data

## Parsing json from a file PART 2

# Use a known good JSON file

f = open ("output5.json", "r")
data2 = json.load(f)
f.close()

print data2

## Parsing json from a file PART 3

# Use a file made up of two known good pieces of JSON one on each line
# But note the whole file is NOT json compliant

with open("output6.json", "r") as f: ## handles opening, closing & memory management
    for line in f:
        jason_string = line.rstrip() ## removes CRs etc...
        data2 = json.loads(jason_string)

print data2

## Parsing json from a file PART 

# Use a test file

filename = raw_input("enter a file name: ")

with open(filename, "r") as f: ## handles opening, closing & memory management
    for line in f:
        jason_string = line.strip() ## removes CRs etc...
        data3 = json.loads(jason_string)

print data3