'''Tasks
Print out all movie titles and their directors.
How long is the longest film? When was it released, 
and what's its original title? Note the data types 
of your values when checking for max() of a value.'''

# My solution without making a .json file... after keep reading the chapter, I now realize the advantage of keeping the information from the API call in a json file, to save money by reducing the API calls... all about money uh! smart! :)
import requests

response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
data = response.json()['data']['films']

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