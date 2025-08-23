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
import os

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

# Lets create a folder to hold all the information (text) extracted in each link
os.makedirs("04_05_wiki_scrape_folders", exist_ok=True)

for idx, url in enumerate(links, 1):
    try:
        sub_request = requests.get(url)
        sub_soup = BeautifulSoup(sub_request.text,"html.parser")

        title_tag = sub_soup.find("title")
        title_text = title_tag.get_text(strip=True) if title_tag else f"article_{idx}" # Get title name, if there is not: title with the index
        
        content_div = sub_soup.find("div", class_="vector-body")
        article_text = content_div.get_text("\n", strip=True) if content_div else ""

        # save file for each link into the folder created before
        filename = f"04_05_wiki_scrape_folders/{idx}_{title_text.replace('/', '_')}.txt" # Just in case title has a '/' ... replace it with a '_'
        with open(filename, "w", encoding="utf-8") as f:
            f.write(article_text)

    except Exception as e:
        print(f"Failed {url}: {e}")