import requests
from bs4 import BeautifulSoup

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

print(titles)