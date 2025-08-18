from Ingredients_project import Ingredient, Spice

class Soup():
    def __init__(self, name, Ingredient,Spice,*Extras):
        self.name = name
        self.Ingredient = Ingredient
        self.Spice = Spice
        self.Extras = Extras

    def cook(self):
        print(f"Let's cook!")
        print(f"The {self.name} has the following ingredients and spice:")
        for ingredient in self.Ingredient:
            print (f" - {ingredient.name} ({ingredient.amount})")
        for spice in self.Spice:
            print (f" - {spice.name} ({spice.amount})")
        if self.Extras:
            print(f" - Extra toppings:")
            for extra in self.Extras:
                print(f"    - {extra}")
        self.serves()
    
    def serves(self):
        for ingredient in self.Ingredient:
            if ingredient.name == "water":
                water_amount = ingredient.amount
                serves = water_amount*2
        print(f"\nServes: {serves}")

# Lets create some ingredients and some spices

blackpepper = Spice("black pepper", 12)
garlic = Spice("garlic cloves", 10)
salt = Spice("salt", 15)
spices = [blackpepper,garlic,salt]

beans = Ingredient("black beans", 30)
water = Ingredient("water", 3)
avocado = Ingredient("avocado", 3)
ingredients = [beans,water,avocado]

# Lets create Hot Black Beans Soup
if __name__ == "__main__":
    beans_soup = Soup("Hot Black Beans Soup",ingredients,spices,"Cheese", "Mushroom", "Pepperoni" )
    beans_soup.cook()