import unittest
from rescrape import *


class TestRescrape(unittest.TestCase):

    # requests can establish a connection and receive a valid response
    def test_get_valid_html_response(self):
        BASE_URL = "https://codingnomads.github.io/recipes/"
        self.assertEqual(get_page_content(BASE_URL).status_code, 200)

    # the response contains HTML code
    def test_get_html_content_returns_html_string(self):
        BASE_URL = "https://codingnomads.github.io/recipes/"
        page = get_html_content(BASE_URL)
        self.assertIn("<!DOCTYPE html>", page)

    # the HTML can be successfully converted to a Beautiful Soup object
    def test_get_bs4_content_returns_bs4_object(self):
        BASE_URL = "https://codingnomads.github.io/recipes/"
        page = get_bs4_object(BASE_URL)
        self.assertIsInstance(page, BeautifulSoup)

    # can identify all links from the index page

    # can identify the author of a recipe

    # can get the main recipe text
    
if __name__ == "__main__":
    unittest.main()
