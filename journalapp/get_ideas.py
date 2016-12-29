#!/usr/bin/env python

import argparse
import json
import sys

def main():
  parser = argparse.ArgumentParser(
      description='Get ideas from file, with optional filter.')
  parser.add_argument('--file', type=file, required=True,
                      help='File containing single JSON object.')
  parser.add_argument('--filter', type=str, required=False,
                      help='Optional filter. Space delimited. Simple "in" matching if provided.')
  args = parser.parse_args()
  lines = args.file.readlines()
  args.file.close()

  previous = ''
  previous2 = ''
  previous3 = ''

  idea_filters = [x.lower() for x in (args.filter or '').split(' ')]
  all_ideas = dict()

  for x in json.loads(lines[0]):
    idea = x['value'].encode('utf8')
    # TODO this is all quite hacky. Clean up.
    idea = idea.replace('##p3 ', '{{ ' + previous3 + ' }} ')
    idea = idea.replace('##p2 ', '{{ ' + previous2 + ' }} ')
    idea = idea.replace('##p ', '{{ ' + previous + ' }} ')
    idea = idea.replace('##P ', '{{ ' + previous + ' }} ')
    idea = idea.replace('#p ', '{{ ' + previous + ' }} ')
    if idea.endswith('##p'):
      idea += '{{ ' + previous + ' }}'


    if 'selected' in x:
      idea = idea.replace('##s ', '{{ ' + all_ideas[x['selected']] + ' }} ')

    all_ideas[x['now']] = idea

    for idea_filter in idea_filters:
      if idea_filter in idea.lower():
        print idea
        break

    previous3 = previous2
    previous2 = previous
    previous = idea

if __name__ == '__main__':
  main()
