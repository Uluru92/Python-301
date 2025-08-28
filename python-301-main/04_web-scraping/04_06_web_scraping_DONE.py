# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup
import os

url = "https://p5aholic.me/projects/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

html_file = "04_06_web_scraping.html"

# Step 1: Fetch the page only if we haven't saved it yet
if not os.path.exists(html_file):
    print("Downloading webpage... (first time only)")
    response = requests.get(url)
    response.raise_for_status()  # raise error if bad status
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(response.text)
else:
    print("Using saved HTML file.")

# Step 2: Load the saved HTML
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

projects_divs = soup.find_all("div", class_="project_item")

for project in projects_divs:
    #  title
    title_tag = project.find("h2", class_="project_title")
    title = title_tag.get_text(strip=True) if title_tag else None

    #  URL
    link_tag = project.find("a", class_="text-btn")
    link = link_tag["href"] if link_tag else None

    #  info <p>
    info_tag = project.find("p", class_="project_info")
    info = info_tag.get_text(strip=True) if info_tag else None

    print(f"Title: {title}")
    print(f"URL: {link}")
    print(f"Info: {info}")
    print("-" * 50)