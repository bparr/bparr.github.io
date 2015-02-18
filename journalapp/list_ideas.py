import json

f = open('2015.01.20.txt')
lines = f.readlines()
f.close()
for x in json.loads(lines[0]):
  print x['value']

