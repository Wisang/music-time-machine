import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import pprint

SPOTIFY_ID = "5c89692e340743159bb461a3986d1b05"
SPOTIFY_SECRET = "be8efc5be4b34859a53d2dd1aac5c22f"
REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               cache_path="token.txt",
                                               scope="playlist-modify-private"))

user = sp.current_user()
user_id = user["id"]

# date_to_go_back = input("which date do you want to go back? YYYY-MM-DD? ")

# URL = "https://www.billboard.com/charts/hot-100/"+date_to_go_back

URL = "https://www.billboard.com/charts/hot-100/2002-01-04"

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")
songs = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", id="title-of-a-story")

titles = []

for song in songs:
    title = song.getText().strip()
    titles.append(title)

song_uris = []

pp = pprint.PrettyPrinter(indent=4)

for title in titles[:10]:
    q = f"track:{title} year:2002"
    try:
        results = sp.search(q, type='track')
        uri = results["tracks"]["items"][0]["uri"]
        # preview = results["tracks"]["items"][0]["preview_url"]
    except IndexError:
        pass
    else:
        song_uris.append(uri)

playlist = sp.user_playlist_create(user=user_id, name="2002 Billboard 100", public=False)
# pp.pprint(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

pp.pprint(sp.playlist(playlist["id"]))
