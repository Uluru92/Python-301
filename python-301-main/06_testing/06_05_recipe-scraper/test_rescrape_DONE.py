import unittest
from rescrape_DONE import *

class TestRescrape(unittest.TestCase):

    # setUp variables for all tests...
    def setUp(self):
        self.BASE_URL = "https://codingnomads.github.io/recipes/"
        self.url = f"{self.BASE_URL}recipes/11-making-my-own-baguet.html"

    # requests can establish a connection and receive a valid response
    def test_get_valid_html_response(self):
        self.assertEqual(get_page_content(BASE_URL).status_code, 200)

    # the response contains HTML code
    def test_get_html_content_returns_html_string(self):
        page = get_html_content(BASE_URL)
        self.assertIn("<!DOCTYPE html>", page)

    # the HTML can be successfully converted to a Beautiful Soup object
    def test_get_bs4_content_returns_bs4_object(self):
        page = get_bs4_object(BASE_URL)
        self.assertIsInstance(page, BeautifulSoup)

    # can identify all links from the index page
    def test_identify_all_links_from_index_page(self):
        links = get_all_links_from_index(BASE_URL)
        self.assertIsInstance(links,list) # Verify we get a list
        self.assertGreater(len(links),0) # Verify the list is not empty
        self.assertIn("recipes/19-wasn-t-sure-how-to-p.html",links) # Verify an existing link

    # can identify the author of a recipe
    def test_can_identify_author(self):

        authors = get_author_from_index(BASE_URL)

        self.assertIsInstance(authors, list) # Verify we get a list
        self.assertGreater(len(authors), 0) # Verify the list is not empty

        for author in authors:
            self.assertIsInstance(author, str) # Verify we get a string
            self.assertFalse(author.lower().startswith("by "))  # Verify the prefix "by " was deleted
            self.assertGreater(len(author.strip()), 0)  # Verify the list is not empty
            self.assertIn("swilliams2207",authors) # Verify an existing author

    # can get titles
    def test_can_identify_titles(self):
        titles = get_titles_from_index(BASE_URL)

        self.assertIsInstance(titles, list)
        self.assertGreater(len(titles), 0)

        for title in titles:
            self.assertIsInstance(title, str)
            self.assertGreater(len(title.strip()), 0)

        self.assertIn("Garlic Butter Steak and Potatoes Skillet", titles)  # ejemplo de título esperado

    # can get the main recipe text
    def test_get_main_recipe_text(self):
        recipes = get_recipes_from_index(BASE_URL)

        self.assertIsInstance(recipes, list) # Verify we get a list
        self.assertGreater(len(recipes), 0) # Verify the list is not empty
        for recipe in recipes:
            self.assertIsInstance(recipe, str)# Verify we get a string
    
if __name__ == "__main__":
    unittest.main()
