animals_of_africa = {
    "aardvark": "a nocturnal badger-sized burrowing mammal",
    "zebra": "a wild horse with black-and-white stripes"
    }

animal = input("Animal to look up: ")

try:
    print(animals_of_africa[animal])
except KeyError:
    print("This animal is not in the database")
