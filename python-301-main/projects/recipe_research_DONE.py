# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

# Solution:

import webbrowser

class Ingredient:
    ''' ingredient info search script. '''
    def __init__(self,name:str, amount:int):
        self.name = name
        self.amount = amount

    def get_info(self,):
        url = f'https://en.wikipedia.org/w/index.php?search=recipe+{self.name}'
        webbrowser.open_new(url)
        return url
    def __add__(self, other):
        url = f'https://en.wikipedia.org/w/index.php?search=recipe+{self.name}+{other.name}'
        webbrowser.open_new(url)
        return 

chesse = Ingredient("mozzarella cheese",1)
chesse.get_info()

spaghetti = Ingredient("spaghetti", 3)
spaghetti.get_info()

tomato = Ingredient("tomato",5)
spinach = Ingredient("spinach", 1)
tomato.__add__(spinach)

