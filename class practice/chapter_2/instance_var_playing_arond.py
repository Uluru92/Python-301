class Ingredient:
    """Models an Ingredient. Currently only carrots!"""

    def __init__(self):
        self.name = "carrot"

i = Ingredient()
c = Ingredient()
jorddy = Ingredient()

# looks like some Polymorphosis down here uh?

print(i.name)  # OUTPUT: carrot
print(c.name)  # OUTPUT: carrot
print(jorddy.name)  # OUTPUT: carrot


class Ingredient_dinner:
    """Models a food item used as an ingredient."""

    def __init__(self, name):
        self.name = name

china = Ingredient_dinner('sushi')
costarica = Ingredient_dinner('pinto')
mexico = Ingredient_dinner('tacos')

print(china.name)
print(costarica.name)
print(mexico.name)