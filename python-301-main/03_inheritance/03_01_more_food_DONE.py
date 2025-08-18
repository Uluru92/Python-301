# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""
    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def expire(self):
        """Expires the ingredient item."""
        if self.name == "salt":
            print(f"{self.name} never expires! ask the sea!")
        else:
            print(f"{self.name} is expired! you better throw it!")
            self.name = "expired " + self.name

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

    def eat_half(self):
        print(f"You have an amount of {self.amount} {self.name}... you are about to eat half...")
        self.amount = self.amount/2
        print(f"YOU ATE HALF the amount of {self.name}! Now you have an amount of {self.amount} {self.name}... ")
    


peas = Ingredient('peas', 12)
pepper = Spice('pepper', 200, "super hot")
salt = Spice("salt", 450,"Regular taste")

peas.expire()
pepper.expire()
salt.expire()

print(peas)
print(pepper)
print(salt)

pepper.grind()
pepper.eat_half()

#p.grind() # we cannot use the method .eat_half() because this method is from the child class, not the parent class Ingredient ;]

# Task 
# Try to instantiate a Spice() object without passing a third argument. What happens? 
#   Anwser: TypeError: Spice.__init__() missing 1 required positional argument: 'taste'
# Try to instantiate an Ingredient() object with a third argument. What error message does Python show you? 
#   Answer: TypeError: Ingredient.__init__() takes 3 positional arguments but 4 were given
# Confirm that you can access .taste on your Spice() object.
print(f"The taste of our ingredient peppers is: {pepper.taste}")
#Try to access .taste on your Ingredient() object. What error message do you get?
#   Answer: AttributeError: 'Ingredient' object has no attribute 'taste'

# Add a second child class if you haven't yet. What else do you need for cooking that could be a child class of either of the two existing classes?
class Vegetable(Ingredient):
    def __init__(self, name, amount, color):
        super().__init__(name, amount)
        self.color = color

    def check_color(self):
        print(f"The {self.name} is color {self.color}")

cucumber = Vegetable("cucumber",10, "green")
cucumber.check_color()