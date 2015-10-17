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

f = open ("problem_1_submission_tst.json", "r")
data2 = json.load(f)
f.close()

print data2