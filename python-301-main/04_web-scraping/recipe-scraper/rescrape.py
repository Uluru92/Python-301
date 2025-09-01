# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.
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

    


if __name__ == "__main__":
    index_html = get_html_content(BASE_URL)
    index_soup = BeautifulSoup(index_html, "html.parser")
    recipe_links = [link["href"] for link in soup.find_all("a")]

    for r_link in recipe_links:
        URL = f"{BASE_URL}/{r_link}"
        html = get_html_content(BASE_URL)
        soup = BeautifulSoup(html, "html.parser")
        author = soup.find("p", class_="author").text.strip("by ")
        recipe = soup.find("div", class_="md").text
        print(f"({author})\t[{recipe}]\n\n\n")
