'''
Extract the title of each recipe and save it as a variable title.
Extract the text body of each recipe and save it as a variable recipe.
Combine the process from the previous lesson and this lesson to access all the information from all recipes.
'''

import requests
from bs4 import BeautifulSoup
import re

url = "https://codingnomads.github.io/recipes/"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
links = soup.find_all("a")

for link in links:
    url_recipe = f'https://codingnomads.github.io/recipes/{link["href"]}'

    page = requests.get(url_recipe)
    soup = BeautifulSoup(page.text,"html.parser")
    #print(soup.prettify() + "\n")

    title = soup.find("h1", class_="title")
    print(f'\nTitle: {title.text}')

    author = soup.find("p", class_="author")
    print(f'Author: {author.text.strip("by ")}')

    ingredients = soup.find_all("p")
    for ingredient in ingredients:
        text = ingredient.text.strip()
        text = re.sub(r"by.*", "", text).strip()
        if text:
            print(f"{text}")

    instructions = soup.find_all("li")
    for instruction in instructions:
        print(f'{instruction.text}')
