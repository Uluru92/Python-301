# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self,name:str,diameter:int,number:int):
        self.name = name
        self.diameter = diameter
        self.number = number

    def __str__(self):
        return f"{self.name} is in the position #{self.number} away from the sun, with a diameter of {self.diameter} kms"
    pass

Mercury = Planet("Mercury", 4.879,1)
Venus = Planet("Venus", 12.104,2)
Earth = Planet("Earth", 12.742,3)
Mars = Planet("Mars", 6.779,4)
Jupiter = Planet("Jupiter", 139.820,5)
Saturn = Planet("Saturn", 116.460,6)
Uranus = Planet("Uranus", 50.724,7)
Neptune = Planet("Neptune", 49.244,8)

list_planets = [Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune]

for planet in list_planets:
    print(planet)
