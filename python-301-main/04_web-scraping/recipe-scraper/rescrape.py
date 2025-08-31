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
BASE_URL = "https://codingnomads.github.io/recipes"

def get_page_content(BASE_URL):
    response = requests.get(BASE_URL)
    return response.status_code

print(get_page_content(BASE_URL))