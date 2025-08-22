# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5
import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

# List of my 6 favorites pokemon:
list_pokemons = ["bulbasaur","charmander","charmeleon","charizard","pidgeotto","pikachu"]

# Lets save each url pokemon in a json file so its easier to extract the info with so
# many calls to the API!...these endpoints are pretty heavy to go throught, my PC was
# about to explode... guess thats another advantage of saving these into files!

for index,pokemon in enumerate(list_pokemons):
    url = f"{BASE_URL}{pokemon}"
    response = requests.get(url)
    data = response.json()
    with open(rf"pokemon_{index+1}.json", "w", encoding="utf-8") as fout:
        json.dump(data, fout, indent=4, ensure_ascii=False)

for index,pokemon in enumerate(list_pokemons):
    with open(rf"pokemon_{index+1}.json", "r") as fin:
        data = json.load(fin)

        print(f"Pokemon name: {data['name']}")
        print(f"Pokemon number: {data['id']}")
        for index,type in enumerate(data["types"]):
            print(f"Pokemon type #{index+1}: {data['types'][index]['type']['name']}")
        print(" ")