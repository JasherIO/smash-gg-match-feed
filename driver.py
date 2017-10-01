#!/usr/bin/env python

import sys
import json
import re
import threading

import scraper


def scrape(opt):
  phases = opt[0]
  interval = opt[1]
  for phase in phases:
    for groupId in phases[phase]:
      phases[phase][groupId] = scraper.sets(groupId)

  
  with open('tournament.json', 'w') as f:
    json.dump(phases, f, indent=2, sort_keys=True)

  threading.Timer(interval, scrape, opt).start()



if __name__ == "__main__":

  # Command Line
  usage = 'Usage: python driver.py tournament-url [interval]'
  defaultInterval = 5

  if len(sys.argv) < 2:
    print usage
    sys.exit()

  url = sys.argv[1]
  interval = sys.argv[2] if sys.argv < 3 else defaultInterval

  match = re.search(r"smash.gg\/(tournament\/)?([\w-]*)\/?", url)
  if not match:
    print 'Error: Invalid URL'
    sys.exit()

  slug = match.group(2)


  # Scraping
  phases = scraper.phases(slug)
  opt = [phases, interval]
  scrape(opt)
