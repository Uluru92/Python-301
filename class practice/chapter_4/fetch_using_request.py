import requests
from bs4 import BeautifulSoup

url = "https://codingnomads.github.io/recipes/"
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text)

links = soup.find_all("a")

# Replace the code above with a Python list comprehension that collects only
# the link URLs in the links variable. You should be able to do this using a
# single line of code.

#Solution:
for link in links:
    print(f'https://codingnomads.github.io/recipes/{link["href"]}')
