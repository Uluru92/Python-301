# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.

# CODE FILE 

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://codingnomads.github.io/recipes/"

def get_page_content(url):
    """Gets the response from a HTTP call to the URL."""
    page = requests.get(url)
    return page

def get_html_content(url):
    response = get_page_content(url)
    html = response.text
    return html

def get_bs4_object(url):
    html = get_html_content(url)
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_all_links_from_index(url):
    index_soup = get_bs4_object(url)
    links = [a["href"] for a in index_soup.find_all("a", href=True)]
    return links

def get_author_from_index(url):
    links = get_all_links_from_index(url)

    authors = []
    for link in links:
        sub_url = url + link
        sub_soup = get_bs4_object(sub_url)
        author_tag = sub_soup.find("p", class_="subtitle is-3 author")
        if author_tag:
            author = author_tag.get_text(strip=True).replace("by ", "", 1)
            authors.append(author)

    return authors

def get_titles_from_index(url):
    links = get_all_links_from_index(url)

    titles = []
    for link in links:
        sub_url = url + link
        sub_soup = get_bs4_object(sub_url)

        title_tag = sub_soup.find("h1", class_="title is-2")
        if title_tag:
            title = title_tag.get_text(strip=True)
            titles.append(title)

    return titles

def get_recipes_from_index(url):
    links = get_all_links_from_index(url)

    recipes = []
    for link in links:
        sub_url = url + link
        sub_soup = get_bs4_object(sub_url)
        recipe_text = sub_soup.find("div", class_="md")
        if recipe_text:
            recipe = recipe_text.text.strip()
            recipes.append(recipe)
    return recipes

if __name__ == "__main__":
    titles = get_titles_from_index(BASE_URL)
    authors = get_author_from_index(BASE_URL)
    recipes = get_recipes_from_index(BASE_URL)

    for title, author, recipe in zip(titles, authors, recipes):
        print(f"Title: {title}\nAuthor: {author}\nRecipe: {recipe}\n")
        print(f"-"*50)
