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

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

# List of my 6 favorites pokemon:
list_pokemons = ["bulbasaur","charmander","charmeleon","charizard","pidgeotto","pikachu"]

for pokemon in list_pokemons:
    url = f"{BASE_URL}{pokemon}"
    print(url)