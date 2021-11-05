#!/bin/python

import sys
import requests
from requests import api

try:
    apikey = sys.argv[1]
    imdb_id = sys.argv[2]
    outfile = sys.argv[3]
except IndexError:
    print("usage: episodes.py [apikey] [imdb_id] [outfile]")
    sys.exit(0)

if sys.argv[1] == "-help" or sys.argv[1] == "--help":
    print("usage: episodes.py [apikey] [imdb_id] [outfile]")
    sys.exit(0)

# retrieve number of seasons
print("fetching number of seasons")
url = f"https://www.omdbapi.com/?i={imdb_id}&apikey={apikey}"
r = requests.get(url)
payload = r.json()
total_seasons = int(payload["totalSeasons"])

# retrieve episode titles
episode_list = []
for i in range(1, total_seasons + 1):
    print(f"fetching episode title for season {i}")
    season = str(i)
    url = f"https://omdbapi.com/?i={imdb_id}&apikey={apikey}&season={season}"
    r = requests.get(url)
    payload = r.json()
    for episode in payload["Episodes"]:
        episode_list.append(episode["Title"].lower())

# write episode files to disk
print(f"writing results to {outfile}")
with open(outfile, "w") as f:
    f.write('\n'.join(episode_list))
