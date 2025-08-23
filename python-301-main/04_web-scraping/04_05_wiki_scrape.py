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

URL = "https://en.wikipedia.org/wiki/Data_extraction"
response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")

with open("04_05_wiki_scrape.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

with open("04_05_wiki_scrape.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
content_div = soup.find("div", class_="mw-content-container")

links = []

for link in content_div.find_all("a", href=True):
    href = link["href"] 

    full_url = href if href.startswith("http") else urljoin(URL, href) # this way we avoid links that keep us in the same page

    if not full_url.startswith("#"):
        links.append(full_url)

for l in links:
    print(l)

'''
for l in links:
    sub_request = requests.get(l)
    sub_soup = BeautifulSoup(sub_request.text,"html.parser")
    sub_title = sub_soup.find("h1", class_="firstHeading mw-first-heading")
    sub_content_div = sub_soup.find("div", class_="mw-content-ltr mw-parser-output")
    print(sub_title)'''