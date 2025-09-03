# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.

# TEST FILE 

from code_06_06_pytest_scraper_DONE import *

BASE_URL = "https://codingnomads.github.io/recipes/"

def test_get_valid_html_response():
    assert get_page_content(BASE_URL).status_code == 200

def test_get_html_content_returns_html_string():
    page = get_html_content(BASE_URL)
    assert ("<!DOCTYPE html>") in page

def test_get_bs4_content_returns_bs4_object():
    page = get_bs4_object(BASE_URL)
    assert isinstance (page,BeautifulSoup)

def test_identify_all_links_from_index_page():
    links = get_all_links_from_index(BASE_URL)
    assert isinstance (links,list)# Verify we get a list
    assert len(links)>0 # Verify the list is not empty
    assert ("recipes/19-wasn-t-sure-how-to-p.html") in links # Verify an existing link

def test_can_identify_author():
    authors = get_author_from_index(BASE_URL)
    assert isinstance (authors, list) # Verify we get a list
    assert len(authors)>0 # Verify the list is not empty
    for author in authors:
            assert isinstance (author, str) # Verify we get a string
            assert not author.lower().startswith("by ")# Verify the prefix "by " was deleted
            assert len(author.strip())>0 # Verify the list is not empty
            assert ("swilliams2207") in authors # Verify an existing author

def test_can_identify_titles():
        titles = get_titles_from_index(BASE_URL)
        assert isinstance(titles, list)
        assert len(titles)> 0
        for title in titles:
            assert isinstance(title, str)
            assert len(title.strip())> 0
        assert ("Garlic Butter Steak and Potatoes Skillet") in titles

def test_get_main_recipe_text():
        recipes = get_recipes_from_index(BASE_URL)
        assert isinstance (recipes, list) # Verify we get a list
        assert len(recipes)> 0 # Verify the list is not empty
        for recipe in recipes:
            assert isinstance (recipe, str) # Verify we get a string