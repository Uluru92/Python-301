class Ingredient:
    """Models an Ingredient. Currently only carrots!"""

    def __init__(self,name: str,quantity: int,measure: str):
        self.name = name
        self.quantity = quantity
        self.measure = measure
    def print_ingredients(self):
        print(f"Ingredient: {self.name}, add {self.quantity} {self.measure}")

mint = Ingredient("mint",10,"leaves")
alcohol = Ingredient("white rum",1.5,"ml")
sugar = Ingredient("white sugar",2,"tea spoons")
lime = Ingredient("lime",0.5,"unit")
soda  = Ingredient("club soda",90,"ml")
ice  = Ingredient("ice",4,"cubes")

print("Recipe for a Mojito Cubano:")
mint.print_ingredients()
alcohol.print_ingredients()
sugar.print_ingredients()
lime.print_ingredients()
soda.print_ingredients()
ice.print_ingredients()