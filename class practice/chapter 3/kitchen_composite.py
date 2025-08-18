class Kitchen():
    def __init__(self, version, Stove, Sink, Fridge, Countertop):
        self.version = version
        self.Stove = Stove
        self.Sink = Sink
        self.Fridge = Fridge
        self.Countertop = Countertop

    def total_price(self):
        total_price = self.Stove.price+self.Sink.price+self.Fridge.price+self.Countertop.price
        print(f"The total price for {self.version} is: {total_price}")

class Stove():
    def __init__(self, price:int, color:str):
        self.price = price
        self.color = color

class Sink():
    def __init__(self, price:int, material:str):
        self.price = price
        self.material = material

class Fridge():
    def __init__(self, price:int, volumen:int):
        self.price = price
        self.volumen = volumen

class Countertop():
    def __init__(self, price:int, surface:int):
        self.price = price
        self.surface = surface

# Create smaller objetcs
stove_option_1 = Stove(900, "yellow")
stove_option_2 = Stove(500, "black")
stove_option_3 = Stove(1500, "red")

sink_option_1 = Sink(850, "wood")
sink_option_2 = Sink(550, "Stainless")
sink_option_3 = Sink(350, "plastic")

fridge_option_1 = Fridge(1500, 1.90)
fridge_option_2 = Fridge(1300, 1.75)
fridge_option_3 = Fridge(1400, 2.00)

countertop_option_1 = Countertop(2150, 5)
countertop_option_2 = Countertop(2050, 3.5)
countertop_option_3 = Countertop(1950, 4)

# Create a larger objet: a composite from smaller objetcs
kitchen_version_1 = Kitchen("version 1", stove_option_1,sink_option_3,fridge_option_2,countertop_option_1)
kitchen_version_2 = Kitchen("version 2", stove_option_2,sink_option_2,fridge_option_3,countertop_option_3)
kitchen_version_3 = Kitchen("version 3", stove_option_3,sink_option_1,fridge_option_1,countertop_option_2)

# Calling a method to get total price of this first composition of smaller objets
kitchen_version_1.total_price()
kitchen_version_2.total_price()
kitchen_version_3.total_price()



