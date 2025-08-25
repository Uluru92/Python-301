class Ingredient:

    """Models a food item used as an ingredient."""
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"

class Spice(Ingredient):
    """Models a spice to flavor your food."""
    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")
    
    def eat_half(self):
        print(f"You have an amount of {self.amount}... you are about to eat half...")
        self.amount = self.amount/2
        print(f"YOU ATE HALF! Now you have an amount of {self.amount}... ")

def practice():
    p = Ingredient('peas', 12)
    print(p)  # OUTPUT: You have 12 peas.
    s = Spice('salt', 200)
    print(s)  # OUTPUT: You have 200 salt.

    s.expire()
    print(s)

    pepper = Spice("pepper", 123)
    pepper.grind()
    # p.grind() ----> # OUTPUT: AttributeError: 'Ingredient' object has no attribute 'grind'

    pepper.eat_half()
    #p.grind() # we cannot use the method .eat_half() because this method is from the child class, not the parent class Ingredient ;]

    class Vegetable(Ingredient):
        def __init__(self, name, amount, color):
            super().__init__(name, amount)
            self.color = color

        def check_color(self):
            print(f"The {self.name} is color {self.color}")

    # Add a second child class if you haven't yet. What else do you need for cooking that could be a child class of either of the two existing classes?
    cucumber = Vegetable("cucumber",10, "green")
    cucumber.check_color()

'''For this project, your task is to create a CLI that takes as input 
the names of ingredients from a user. Then, your code will fetch the 
recipe information from the CodingNomads recipe collection and search
 through the text of the recipes to find ones that include the provided 
 ingredients.'''

if __name__ == "__main__":  
    print("Ok now is your turn to participate user! Give me 3 ingredients to built a recipe!")
    Ingredient_by_user_1 = input("Ingrediente 1: ")
    Ingredient_by_user_2 = input("Ingrediente 2: ")
    Ingredient_by_user_3 = input("Ingrediente 3: ")

