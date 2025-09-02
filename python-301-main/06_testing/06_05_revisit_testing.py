# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.

# I am going to revisit the previous exercise 04_03_poke_info!
# ok... 

''''# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
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
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5'''

import unittest
import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

class TestAssembleTeam(unittest.TestCase):
    # setUp variables for all tests...
    def setUp(self):
        self.BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
        self.list_pokemons = ["bulbasaur","charmander","charmeleon","charizard","pidgeotto","pikachu"]
    
