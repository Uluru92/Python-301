# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.

# I am going to revisit the previous exercise 04_03_poke_info!

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
import os

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
list_pokemons = ["bulbasaur","charmander","charmeleon","charizard","pidgeotto","pikachu"]

def create_folder_to_keep_json_files(path):
    os.makedirs('files_exercise_06_05', exist_ok=True)
    return True

def get_response(url):
    response = requests.get(url)
    return response

def get_data_json_from_response(url):
    response = get_response(url)
    data = response.json()
    return data

def save_data_json_in_file_json(path, data):
    with open(path, "w", encoding="utf-8") as fout:
        json.dump(data, fout, indent=4, ensure_ascii=False)
    return path

create_folder_to_keep_json_files('files_exercise_06_05')

for index,pokemon in enumerate(list_pokemons):
    url = f"{BASE_URL}{pokemon}"
    data = get_data_json_from_response(url)
    save_data_json_in_file_json(rf"files_exercise_06_05\pokemon_{index+1}.json",data)

class TestAssembleTeam(unittest.TestCase):
    # setUp variables for all tests...
    def setUp(self):
        self.BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
        self.list_pokemons = ["bulbasaur","charmander","charmeleon","charizard","pidgeotto","pikachu"]
    
    # Check if my list have all 6 pokemons
    def test_my_len_list(self):
        self.assertEqual(len(self.list_pokemons),6)

    # Check if the response is ok (200)
    def test_get_response_200(self):
        self.assertEqual(get_response(BASE_URL).status_code,200)

    # Check if the response was transforme to a .json data
    def test_get_data_json_from_response(self):
        data = get_data_json_from_response(BASE_URL)
        self.assertIsInstance(data, (dict, list))

    # Check if the data json was saved in a .json file
    def test_data_json_saved_in_json_file(self):
        test_path = "test.json"
        test_data = {"name": "pikachu"}
        output = save_data_json_in_file_json(test_path, test_data)

        # check return value
        self.assertEqual(output, test_path)

        # check file exists and content is correct
        with open(test_path, "r",encoding="utf-8") as f:
            saved_data = json.load(f)
        self.assertEqual(saved_data, test_data)
        
if __name__ == "__main__":
    unittest.main()