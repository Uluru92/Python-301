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
    
c = Ingredient("carrot", 5)

print(c)  # OUTPUT: carrot (5)
print(repr(c))  # OUTPUT: Ingredient(name=carrot, amount=5)