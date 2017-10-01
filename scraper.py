# Author: Joshua C. Willis
# License: MIT
# Copyright: 2017

import requests
import json
import sys

import parser

def phases(slug):
  base = 'https://api.smash.gg/tournament/'
  expands = '?expand[]=phase&expand[]=groups'
  url = base + slug + expands

  r = requests.get(url)
  tournament = json.loads(r.text)

  if (r.status_code != 200):
    print 'Error: tournament "{}" invalid'.format(slug)
    sys.exit()

  phases = {}
  parsed = parser.phases(tournament['entities']['phase'])
  for id, name in parsed.items():
    # Group IDs for this phase
    groupIds = [group['id'] for group in tournament['entities']['groups'] if group['phaseId'] == id]
    for groupId in groupIds:
      if name in phases:
        phases[name][groupId] = {}
      else:
        phases[name] = { groupId: {} }

  return phases


def sets(groupId):

  base = 'https://api.smash.gg/phase_group/'
  expands = '?expand[]=entrants&expand[]=sets'

  url = base + str(groupId) + expands
  r = requests.get(url)

  if (r.status_code != 200):
    print 'Error: group "{}" invalid'.format(groupId)
    sys.exit()

  group = json.loads(r.text)

  entrants = parser.entrants(group['entities']['entrants'])
  return {
    group['entities']['groups']['identifier']: parser.sets(group['entities']['sets'], entrants)
  }
  