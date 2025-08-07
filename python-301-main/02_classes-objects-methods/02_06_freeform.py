# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class HairItems():
    def __init__(self, name:str, cost:int, amount:int):
        self.name = name
        self.cost = cost
        self.amount = amount

    def __str__(self):
        return (
            f"Item: {self.name}\n"
            f"Cost: ${self.cost}\n"
            f"Quantity: {self.amount} units\n"
        )
    
    def __add__(self,other):
        new_name = self.name + " and " + other.name
        new_amount = self.amount + other.amount
        new_cost = self.cost + other.cost
        return HairItems(new_name, new_amount, new_cost)
    
hair_brushes = HairItems("Yellow brush", 12, 1)
print(HairItems)

hair_dryer = HairItems("hair dryer", 20, 1)



class Water():
    def __init__(self, liters:int, color:str, source:str, name:str="water"):
        self.liters = liters
        self.color = color
        self.name = name
        self.source = source

    def __str__(self):
        return (
            f"Item: {self.name}\n"
            f"Liters: {self.liters} L\n"
            f"Color: {self.color}\n"
        )

    def __add__(self,other):
        new_liters = self.liters + other.liters
        if self.color == "transparent":
            new_color = other.color
        if self.color == "transparent" and other.color == "transparent":
            new_color = "transparent"
        if self.color == "brown":
            new_color = "brown"
            self.name = "Dirty water"
        return Water(new_liters, new_color,self.name)
    
    def refill(self, new_liters):
        self.liters += new_liters
        return print(f"You added {new_liters} liters to {self.source} {self.name}, now there are {self.liters} liters of {self.source} {self.name} ")

# Instantiating objets from blueprint
tap_water = Water(2,"brown","tap")
bottle_water = Water(5,"transparent", "bottle")
drilled_water = Water(20, "transparent", "drilled")

# Chaging an attribute value through a method
tap_water.refill(4)
bottle_water.refill(8)
drilled_water.refill(10)

# __add__ function
print(f"\nTap water mixed with Bottle water:\n{tap_water + bottle_water}")
print(f"Tap water mixed with Drilled water:\n{tap_water + drilled_water}")
print(f"Bottle water mixed with Drilled water:\n{bottle_water + drilled_water}")

