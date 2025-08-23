# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

# Solution:

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://en.wikipedia.org/wiki/Web_scraping"
request = requests.get(URL)
soup = BeautifulSoup(request.text,"html.parser")

content_div = soup.find("div", class_="mw-content-container")

links = soup.find_all("a",href=True)

links = []
if content_div:
    for link in content_div.find_all("a", href=True):
        href = link["href"]
        if href.startswith("http://") or href.startswith("https://"):
            full_url = href

        else:
            full_url = urljoin(URL, href)  # make url absolute
        
        if not full_url.startswith("#"):  # skip fragments that stays on same page
            links.append(full_url)

for l in links:
    sub_request = requests.get(l)
    sub_soup = BeautifulSoup(sub_request.text,"html.parser")
    sub_title = sub_soup.find("h1", class_="firstHeading mw-first-heading")
    sub_content_div = sub_soup.find("div", class_="mw-content-ltr mw-parser-output")