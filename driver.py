#!/usr/bin/env python

import sys
import json
import re
import threading

import scraper


defaultInterval = 5
interval = defaultInterval
phases = {}

def scrape():
  for phase in phases:
    for groupId in phases[phase]:
      phases[phase][groupId] = scraper.sets(groupId)

  with open('tournament.json', 'w') as f:
    json.dump(phases, f, indent=2, sort_keys=True)

  threading.Timer(interval, scrape).start()


if __name__ == "__main__":

  # Command Line
  usage = 'Usage: python driver.py tournament-url [interval]'

  if len(sys.argv) < 2:
    print usage
    sys.exit()

  url = sys.argv[1]

  if len(sys.argv) >= 3:
    interval = int(sys.argv[2])

  match = re.search(r"smash.gg\/(tournament\/)?([\w-]*)\/?", url)
  if not match:
    print 'Error: Invalid URL'
    sys.exit()

  slug = match.group(2)


  print 'Press CTRL+C to exit'

  # Scraping
  phases = scraper.phases(slug)
  scrape()
