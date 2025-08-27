# Demonstrate how you can log in to the Reddit API to receive content that
# requires authentication, using only `requests` and your credentials.

import requests.auth
import os
import json

from dotenv import load_dotenv

load_dotenv()

password = os.getenv("password")
username = os.getenv("username")
client_secret = os.getenv("client_secret")
client_id = os.getenv("client_id")

client_auth = requests.auth.HTTPBasicAuth(f'{client_id}', f'{client_secret}')
post_data = {"grant_type": "password", "username": "Uluru1992", "password": password}
headers = {"User-Agent": f"ChangeMeClient/0.1 by u/Uluru1992"}
response = requests.post(
    "https://www.reddit.com/api/v1/access_token",
    auth=client_auth,
    data=post_data,
    headers=headers
    )

print(response.json())

'''output: {'access_token': 'erased by me hehe', 'token_type': 'bearer',
 'expires_in': 86400, 'scope': '*'}'''


# Nos lets use it to get some info! 
headers = {
    "Authorization": f"bearer {response.json()['access_token']}",
    "User-Agent": "mytestapp/0.1 by u/Uluru1992"
}

url = "https://oauth.reddit.com/r/python/hot" # Get hot posts from a subreddit
response = requests.get(url, headers=headers)
token_data = response.json()

# To demostrate the log in, lets save the info in a .json file
with open(r"python-301-main\projects\make-recipe-page\redditapi-get-token.json", "w") as f:
    json.dump(token_data, f, indent=4)