#!/usr/bin/env python

import argparse
import json


def main():
  parser = argparse.ArgumentParser(
      description='Combine multiple idea exports into one.')
  parser.add_argument('--file', type=file, required=True,
                      help='File containing all idea exports (one per line).')
  args = parser.parse_args()
  lines = args.file.readlines()
  args.file.close()

  all_ideas = {}
  for i, line in enumerate(lines):
    if not line.strip():
      continue
    try:
      parsed = json.loads(line)
    except:
      print line
      raise

    for idea in parsed:
      if idea['now'] in all_ideas and idea['value'] != all_ideas[idea['now']]:
        raise 'Mismatched idea values!'
      all_ideas[idea['now']] = idea['value']

  all_ideas_list = [{'now': x, 'value': y} for x,y in all_ideas.iteritems()]
  print json.dumps(sorted(all_ideas_list, key=lambda x: x['now']),
                   separators=(',', ':'))

if __name__ == '__main__':
  main()
