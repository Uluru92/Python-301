# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

import os
import praw
import json
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("client_id"),
    client_secret=os.getenv("client_secret"),
    username=os.getenv("user_name"),
    password=os.getenv("password"),
    user_agent="python:recipes:v1.0 (by u/Uluru1992)"
)

subreddit = reddit.subreddit("recipes")
recipes = []

for post in subreddit.hot(limit=100): 
    # Skip posts with no text and only image links
    if not post.selftext.strip() and not post.url.endswith(".jpeg"):
        post.comments.replace_more(limit=0)  # load all top-level comments
        recipe_comment = None

        # Look for the OP's comment, where usually the recipe/ingredients/methods are
        for comment in post.comments:
            if comment.author == post.author and len(comment.body.strip()) > 50:
                recipe_comment = comment.body.strip()
                break

        # --- Clean duplicate lines ---
        if recipe_comment:
            lines = recipe_comment.splitlines()
            cleaned_lines = []
            for line in lines:
                if line.strip() not in cleaned_lines:
                    cleaned_lines.append(line.strip())
            recipe_comment = "\n".join(cleaned_lines)  # replace with cleaned text

        # Append to recipes
        if recipe_comment:
            recipes.append({
                "title": post.title,
                "reddit_link": f"https://reddit.com{post.permalink}",
                "recipe_text": recipe_comment
            })

    if len(recipes) == 5:
        break

# Print recipes
for r in recipes:
    print(r["title"])
    print(r["reddit_link"])
    print(r["recipe_text"])  # preview first 300 chars
    print("-" * 50)

# Save recipes to JSON
with open("reddit_recipes.json", "w", encoding="utf-8") as f:
    json.dump(recipes, f, indent=4, ensure_ascii=False)

print("Saved recipes to reddit_recipes.json")