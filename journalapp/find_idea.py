import json
import sys

to_find = sys.argv[1]
print to_find

f = open('2015.01.20.txt')
lines = f.readlines()
f.close()
for x in json.loads(lines[0]):
  value = x['value']
  if to_find in value:
    print value

