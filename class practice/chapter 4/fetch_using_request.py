import requests

BASE_URL = "https://codingnomads.github.io/recipes/"
page = requests.get(BASE_URL)
print(page)
print(page.text)