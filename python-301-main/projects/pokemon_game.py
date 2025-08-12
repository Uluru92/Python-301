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
    def __init__(self, name:str, primary_type: str, max_hp:int, hp:int):
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = hp
        pass

    def __str__(self):
        return (
            f"Pokemon name: {self.name}"
            f"Pokemon type: {self.primary_type}"
            f"Pokemon HP: {self.hp}/{self.max_hp}"
        )

    def battle(self, other):
        pokemon_1 = self.name
        pokemon_2 = other.name

        logic_type = ["water":3, "fire":6, "grass":9]
        logic_end = ["won":0, "lost":1, "tied":2]

        
        
        pass

    def feed(self):
        if self.hp < self.max_hp:
            self.hp +=1
            print(f"Health restored +1 points. Actual HP: ({self.hp})/({self.max_hp})")
        else:
            print(f"{self.name} is already at full HP")