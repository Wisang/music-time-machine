import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = "5c89692e340743159bb461a3986d1b05"
SPOTIFY_SECRET = "be8efc5be4b34859a53d2dd1aac5c22f"
REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private"))

user = sp.current_user()
user_id = user["id"]

# date_to_go_back = input("which date do you want to go back? YYYY-MM-DD? ")

# URL = "https://www.billboard.com/charts/hot-100/"+date_to_go_back

URL = "https://www.billboard.com/charts/hot-100/2002-01-04"

# response = requests.get(URL)
#
# html = response.text
#
# soup = BeautifulSoup(html, "html.parser")
#
# songs = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", id="title-of-a-story")
#
# titles = []
#
# for song in songs:
#     title = song.getText().strip()
#     titles.append(title)
#
# print(titles)