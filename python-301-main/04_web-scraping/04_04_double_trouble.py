# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

# Solution: I will follow the recomendation but with cats -> Ghibli Cats vs My 6 Favorites Pokemons!

import requests

cats_url = []

url_SG = "https://ghibliapi-iansedano.vercel.app/api/species"
response = requests.get(url_SG)
data = response.json()

for specie in data['data']['species']:
    if specie['name'] == "Cat":
        cats_url = specie['people']

for link in cats_url:
    print(link)