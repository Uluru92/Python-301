# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup
import os

URL = "https://p5aholic.me/projects/"
HTML_FILE = "04_06_web_scraping.html"

def fetch_html(url=URL, html_file=HTML_FILE):
    """Fetch HTML from the web if not cached, otherwise use local file."""
    if not os.path.exists(html_file):
        print("Downloading webpage...")
        response = requests.get(url)
        response.raise_for_status()
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(response.text)
    else:
        print("Using saved HTML file.")

    with open(html_file, "r", encoding="utf-8") as f:
        return f.read()

def parse_projects(html_content):
    """Parse HTML and extract project info into a list of dicts."""
    soup = BeautifulSoup(html_content, "html.parser")
    projects_divs = soup.find_all("div", class_="project_item")

    projects = []
    for project in projects_divs:
        title = project.find("h2", class_="project_title")
        link = project.find("a", class_="text-btn")
        info = project.find("p", class_="project_info")

        projects.append({
            "title": title.get_text(strip=True) if title else None,
            "url": link["href"] if link else None,
            "info": info.get_text(strip=True) if info else None
        })
    return projects

def display_projects(projects):
    """Print project info nicely."""
    for p in projects:
        print(f"Title: {p['title']}")
        print(f"URL: {p['url']}")
        print(f"Info: {p['info']}")
        print("-" * 50)

def main():
    html = fetch_html()
    projects = parse_projects(html)
    display_projects(projects)

if __name__ == "__main__":
    main()