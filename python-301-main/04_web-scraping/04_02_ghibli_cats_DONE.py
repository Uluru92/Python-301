# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi-iansedano.vercel.app/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.
# Solution:

import requests
BASE_URL = "https://ghibliapi-iansedano.vercel.app/api/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3"

page = requests.get(BASE_URL)
data = page.json()
links = data["data"][0]["people"]

for index,link in enumerate(links,start = 1):
    print(f"\nCat #{index}")
    page_cat = requests.get(link)
    data = page_cat.json()
    name = data["data"][0]["name"]
    gender = data["data"][0]["gender"]
    age = data["data"][0]["age"]
    eye_color = data["data"][0]["eye_color"]
    hair_color = data["data"][0]["hair_color"]
    print(f'Name: {name}')
    print(f'Gender: {gender}')
    print(f'Age: {age}')
    print(f'Eye color: {eye_color}')
    print(f'Hair color: {hair_color}')