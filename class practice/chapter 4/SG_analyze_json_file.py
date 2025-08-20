'''Studying data from Studio Ghibli API json file,
this file was created in another script py file before,
this way, we avoid making lots of calls to an API,
this method is used to save money $$$'''

import json

with open(r"class practice\chapter 4\films.json", "r") as fin:
    data = json.load(fin)

running_time_dictionary= {}

for dictionary in data:
    print(f'Title: {dictionary["title"]} - Director: {dictionary["director"]}')
    running_time = int(dictionary["running_time"])
    running_time_dictionary[dictionary["title"]] = running_time

longest_movie = max(running_time_dictionary, key=running_time_dictionary.get)
print(f"\nLongest movie: {longest_movie} - {running_time_dictionary[longest_movie]} minutes")

for dictionary in data:
    if dictionary["title"] == longest_movie:
        original_title = dictionary["original_title"]
        print(f"The original title was {original_title}")