'''Extracting data from Studio Ghibli API and putting into a json file '''

import json
import requests

response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
data = response.json()['data']['films']


#with open(r"C:\Users\jordd\Documents\Repositorios Github\Python-301\class practice\chapter 4\films.json", "w") as fout:
with open(r"class practice\chapter 4\films.json", "w") as fout:
    json.dump(data, fout)