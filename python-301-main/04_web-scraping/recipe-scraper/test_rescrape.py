import unittest
from rescrape import *


class TestRescrape(unittest.TestCase):

    # requests can establish a connection and receive a valid response
    def test_get_valid_html_response(self):
        BASE_URL = "https://codingnomads.github.io/recipes/"
        index_page = rescrape.get_page_content(BASE_URL)
        self.assertEqual(index_page.status_code, 200)

    # the response contains HTML code

    # the HTML can be successfully converted to a Beautiful Soup object

    # can identify all links from the index page

    # can identify the author of a recipe

    # can get the main recipe text

    pass

if __name__ == "__main__":
    unittest.main()
