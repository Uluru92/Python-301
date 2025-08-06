class Ingredient:
    """Models an Ingredient. Currently only carrots!"""

    def __init__(self,name: str,quantity: int,measure: str, id:int):
        self.name = name
        self.quantity = quantity
        self.measure = measure
        self.id = id
    def print_ingredient(self):
        print(f"Ingredient {self.id}: {self.name}, add {self.quantity} {self.measure}")

    def expire(constructor):
        """Expires the ingredient."""
        print(f"whoops, these {constructor.name} went bad...")
        constructor.name = "expired " + constructor.name

mint = Ingredient("mint",10,"leaves",1)
alcohol = Ingredient("white rum",1.5,"ml",2)
sugar = Ingredient("white sugar",2,"tea spoons",3)
lime = Ingredient("lime",0.5,"unit",4)
soda  = Ingredient("club soda",90,"ml",5)
ice  = Ingredient("ice",4,"cubes",6)

print("Recipe for a Mojito Cubano:")
mint.print_ingredient()
alcohol.print_ingredient()
sugar.print_ingredient()
lime.print_ingredient()
soda.print_ingredient()
ice.print_ingredient()

print("Checking quality of ingredients:")
lime.expire()
print(lime.name)
