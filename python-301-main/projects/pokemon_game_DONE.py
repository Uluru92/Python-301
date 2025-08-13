# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`


class Pokemon:
    def __init__(self, name:str, primary_type: str, hp:int):
        self.name = name
        self.primary_type = primary_type
        self.hp = hp
        self.max_hp = hp

        pass

    def __str__(self):
        return (
            f"Pokemon name: {self.name}"
            f"Pokemon type: {self.primary_type}"
            f"Pokemon HP: {self.hp}/{self.max_hp}"
        )

    def battle(self, other):
        print(f"Battle: {self.name} vs {other.name}!")
        result = self.typewheel(self.primary_type, other.primary_type)
        print(f"Pokemon {self.name} has {result} the match!")
        if result == "won":
            other.hp -= 10
            print(f"- {other.name} has lost 10 health points, resulting with {other.hp}/{other.max_hp} HP\n")
        elif result == "lost":
            self.hp -= 10
            print(f"- {self.name} has lost 10 health points, resulting with {self.hp}/{self.max_hp} HP\n")
        else:
            self.hp -= 5
            other.hp -= 5
            print(f"- Both fighters lost 5 health points.")
            print(f"- {self.name} resulting with {self.hp}/{self.max_hp} HP.")
            print(f"- {other.name} resulting with {other.hp}/{other.max_hp} HP.")
            print(" ")
            pass

    @staticmethod
    def typewheel (type1, type2):
        logic_type = {"water":0, "fire":1, "grass":2}
        logic_result = {0:"won", 1:"lost", 2:"tied"}

        win_lose_matrix = [
            [2,0,1], # Position 1: water
            [1,2,0], # Position 2: fire
            [0,1,2]  # Position 3: grass
            ]
        
        win_lose_result = win_lose_matrix[logic_type[type1]][logic_type[type2]]
        return logic_result[win_lose_result]
         
    def feed(self):
        if self.hp < self.max_hp:
            self.hp +=1
            print(f"{self.name} was feed propertly. Health restored +1 points. Actual HP: ({self.hp})/({self.max_hp})")
        else:
            print(f"{self.name} was feed, thought it's already at full HP")

# LETS CREATE SOME POKEMONS FROM OUR CLASS!
water_dude = Pokemon("Water dude", "water", 100)
water_kid = Pokemon("Water kid", "water", 100)
fire_dragon = Pokemon("Fire dragon", "fire", 100)
fire_woman = Pokemon("Fire woman", "fire", 100)
grass_horse = Pokemon("Grass horse", "grass", 100)
grass_bird = Pokemon("Grass bird", "grass", 100)

# LETS BATTLE!
water_dude.battle(water_kid)
fire_dragon.battle(grass_horse)
grass_bird.battle(water_kid)

# LETS FEED SOME POKEMONS
grass_horse.feed()
fire_dragon.feed()

