# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.import requests

from bs4 import BeautifulSoup
import requests
import os

if __name__ == "__main__":  

    url_recipes = "https://codingnomads.github.io/recipes/"
    response = requests.get(url_recipes)

    # Lets create a folder to hold all the information (text) extracted in each link!
    os.makedirs("Recipe_Collection", exist_ok=True)

    # Lets create the html of the main page recipes codingNomads!
    data = requests.get(url_recipes)
    soup = BeautifulSoup(data.text,"html.parser")

    with open(r"Recipe_Collection\recipes_cn.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    # Lets create the list of links inside the main page, to analize them later!    
    with open(r"Recipe_Collection\recipes_cn.html", "r", encoding="utf-8") as f:
        html = f.read()

    soup_html = BeautifulSoup(html, "html.parser")
    tags_a = soup_html.find_all("a", href=True)

    recipe_links = []

    for tag in tags_a:
        recipe_links.append(f"https://codingnomads.github.io/recipes/{tag['href']}")
    
    # Lets ask the user to provide 3 ingredients so we can search recipes with them in each link
    print("Ok now is your turn to participate user! Give me 3 ingredients to built a recipe!")
    Ingredient_by_user_1 = input("Ingrediente 1: ").lower()
    Ingredient_by_user_2 = input("Ingrediente 2: ").lower()
    Ingredient_by_user_3 = input("Ingrediente 3: ").lower()
    ingredients = [Ingredient_by_user_1, Ingredient_by_user_2, Ingredient_by_user_3]

    # Lets analize link by link searching for ingredients provided by user!
    found = False
    for index,link in enumerate(recipe_links):

        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        tags_p = soup.find_all("p")
        all_text = ""
        for p in tags_p:
            classes = p.get("class", [])
            if "subtitle" in classes and "author" in classes:
                continue
            all_text += p.get_text().lower() + " "
        
        author_tag = soup.find("p", class_="subtitle is-3 author")
        if author_tag:
            author = author_tag.get_text().strip()
            if author.lower().startswith("by "):
                author = author[3:].strip()  # elimina "by " al inicio
            # También eliminamos de all_text si empieza con "by <author>"
            if all_text.lower().startswith(f"by {author.lower()}"):
                all_text = all_text[len(f"by {author.lower()}"):].strip()
        else:
            author = "Author not found"

        for ingredient in ingredients:
            if ingredient in all_text:
                print(f"✅ Found '{ingredient}' in the link {link}:")
                title = soup.find("title").get_text()
                clean_title = title.split(" by ")[0]
                print(f"Title: {clean_title}")
                print("Author:", author)
                print("Text preview:\n", all_text)
                print(" ")
                found = True
    
    if not found:
        print("❌ No ingredients found") 