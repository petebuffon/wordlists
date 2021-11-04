import sys
import requests

try:
    api_key = sys.argv[1]
    imdb_id = sys.argv[2]
    outfile = sys.argv[3]
except IndexError:
    print("usage: episodes.py [api_key] [imdb_id] [outfile]")
    sys.exit(0)

if sys.argv[1] == "-help" or sys.argv[1] == "--help":
    print("usage: episodes.py [api_key] [imdb_id] [outfile]")
    sys.exit(0)

# retrieve number of seasons
print("fetching number of seasons")
url = f"https://imdb-api.com/en/API/Title/{api_key}/{imdb_id}"
r = requests.get(url)
payload = r.json()
seasons = len(payload["tvSeriesInfo"]["seasons"])

# retrieve episode titles
episode_list = []
for i in range(1,seasons):
    print(f"fetching episode title for season {i}")
    url = "https://imdb-api.com/en/API/SeasonEpisodes/k_vpc4r8s5/tt0411008/" + str(i)
    json_payload = requests.get(url)
    episodes = json_payload.json()
    for episode in episodes["episodes"]:
        episode_list.append(episode["title"])

# write episode files to disk
print(f"writing results to {outfile}")
with open(outfile, "w") as f:
    f.write('\n'.join(episode_list))
