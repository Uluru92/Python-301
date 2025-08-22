# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

# Solution: I will follow the recomendation but to blend 6 Ghibli Cats with My 6 Favorites Pokemons and create new creatures!

from pprint import pprint
import requests
import random
import json

# Create class for each Cat and each Pokemon
class Character():
        pass

class Cat(Character):
    def __init__(self,name, eye_color:str, hair_color:str):
        self.name = name
        self.eye_color = eye_color
        self.hair_color = hair_color
    
    def __str__(self):
        return (f"Cat Name: {self.name}\nCat Eye Color: {self.eye_color}\nCat Hair Color: {self.hair_color}")

class Pokemon(Character):
    def __init__(self,name:str,number:int,type:str):
        self.name = name
        self.number = number
        self.type = type

    def __str__(self):
            return (f"Pokemon Name: {self.name}\nPokemon Number: {self.number}\nPokemon Type: {self.type}")
        

class FusionCharacter(Character):
    def __init__(self, cat: Cat, pokemon: Pokemon):
        self.cat = cat
        self.pokemon = pokemon
        self.name = f"{cat.name}-{pokemon.name}"
        self.eye_color = cat.eye_color
        self.hair_color = cat.hair_color
        self.pokemon_type = pokemon.type

    def __str__(self):
        return (
            "These two characters are about to merge in one new creature!\n\n"
            f"Cat:\nName: {self.cat.name}\nEye Color: {self.cat.eye_color}\nHair Color: {self.cat.hair_color}\n\n"
            f"Pokemon:\nName: {self.pokemon.name}\nNumber: {self.pokemon.number}\nType: {self.pokemon.type}\n\n"
            f"Result:\nFusionCharacter:\nName: {self.name}\nEye Color: {self.eye_color}\nHair Color: {self.hair_color}\nType: {self.pokemon_type}"
        )
    
cats_url = []

url_SG = "https://ghibliapi-iansedano.vercel.app/api/species"
response = requests.get(url_SG)
data = response.json()

# Get url list of all cats:
for specie in data['data']['species']:
    if specie['name'] == "Cat":
        cats_url.extend(specie['people'])

# Select only 6 random url cats:
cats_url_selected = random.sample(cats_url, 6)

for index,cat_url in enumerate(cats_url_selected):
    url = f"{cat_url}"
    response = requests.get(cat_url)
    data = response.json()
    with open(rf"cat_{index+1}.json", "w", encoding="utf-8") as fout:
        json.dump(data, fout, indent=4, ensure_ascii=False)

cats_objects = [] # Here we collect all the cat objects to use them later!

for index,pokemon in enumerate(cats_url_selected):
    with open(rf"cat_{index+1}.json", "r") as fin:
        data = json.load(fin)

        cat_name =  data['data'][0]['name']
        cat_eye_color = data['data'][0]['eye_color']
        cat_hair_color = data['data'][0]['hair_color']

        cat_obj = Cat(cat_name,cat_eye_color,cat_hair_color)
        cats_objects.append(cat_obj)

# Create 6 cats! Everytime they are going to be different because we are picking random cats from the whole!
cat_1 = cats_objects[0]
cat_2 = cats_objects[1]
cat_3 = cats_objects[2]
cat_4 = cats_objects[3]
cat_5 = cats_objects[4]
cat_6 = cats_objects[5]

# Create 6 pokemons (from exercise before...)
list_pokemons = ["bulbasaur","charmander","charmeleon","charizard","pidgeotto","pikachu"]
pokemon_objects = [] # Here we collect all the pokemon objects to use them later!

for index,pokemon in enumerate(list_pokemons):
    with open(rf"pokemon_{index+1}.json", "r") as fin:
        data = json.load(fin)

        pokemon_name = data['name']
        pokemon_number = data['id']
        types_list = [poke_type['type']['name'] for poke_type in data["types"]] # we pick a random type if the pokemon has more than 1 type
        pokemon_type = random.choice(types_list)

        poke_obj = Pokemon(pokemon_name,pokemon_number,pokemon_type)
        pokemon_objects.append(poke_obj)

pokemon_1 = pokemon_objects[0]
pokemon_2 = pokemon_objects[1]
pokemon_3 = pokemon_objects[2]
pokemon_4 = pokemon_objects[3]
pokemon_5 = pokemon_objects[4]
pokemon_6 = pokemon_objects[5]

poke_cat_1 = FusionCharacter(cat_1,pokemon_1)
print(poke_cat_1)


        
