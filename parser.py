# Author: Joshua C. Willis
# License: MIT
# Copyright: 2017

def entrants(data):
  entrants = {}

  for entrant in data:
    id = entrant['id']
    name = entrant['name']

    entrants[id] = name

  return entrants


def phases(data):
  phases = {}

  for phase in data:
    id = phase['id']
    name = phase['name']

    phases[id] = name

  return phases


def sets(data, entrants):
  sets = {}
  for set in data:
    round = set['round']
    entrant1Id = set['entrant1Id']
    entrant1Score = str(set['entrant1Score'])
    entrant2Id = set['entrant2Id']
    entrant2Score = str(set['entrant2Score'])

    if (not (entrant1Id and entrant2Id)):
      continue

    entrant1Name = entrants[entrant1Id]
    entrant2Name = entrants[entrant2Id]

    match = '{} {}-{} {}'.format(entrant1Name, entrant1Score, entrant2Score, entrant2Name)
    if round not in sets:
      sets[round] = [match]
    else:
      sets[round].append(match)

  return sets
