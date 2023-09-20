import requests
from bs4 import BeautifulSoup

url="https://news.ycombinator.com/"
response = requests.get(url)
soup=BeautifulSoup(response.text)
for link in soup.find_all('a'):
    foundlink=link.get("href")
    if "https" in foundlink:
        print(foundlink)
