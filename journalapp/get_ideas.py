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
                      help='Optional filter. Simple "in" matching if provided.')
  args = parser.parse_args()
  lines = args.file.readlines()
  args.file.close()

  for x in json.loads(lines[0]):
    idea = x['value'].encode('utf8')
    if args.filter is None or args.filter in idea:
      print idea

if __name__ == '__main__':
  main()
