#!/usr/bin/env python

import requests
import json

# url = 'https://smash.gg/tournament/nexus-gaming-saturday-150-na-3v3-weekly-tournament-36/details'

base = 'https://api.smash.gg/tournament/nexus-gaming-saturday-150-na-3v3-weekly-tournament-36'
expands = '?expand[]=groups'
url = base + expands

r = requests.get(url)
tournament = json.loads(r.text)
# print json.dumps(tournament, indent=2, sort_keys=True)

groups = map(lambda x: x['id'], tournament['entities']['groups'])
print groups