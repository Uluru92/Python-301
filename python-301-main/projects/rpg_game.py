# Project RPG GAME! - Chapter 2:

# Lets create some classes!
class Character:
    '''A base character... with this class, its born:
    The Hero - Main Character: Player
    The Monsters that need to be killed
    The Allies of the Hero as secondary chars
    Any other secondary character in the game...!'''

    def __init__(self, name:str, hp_max:int, hp:int, magic_resist:int, armor:int, strenght: int, mana:int, agility:int, level:int, experience:int ):
        self.name = name
        self.hp_max = hp_max
        self.hp = hp
        self.magic_resist = magic_resist
        self.armor = armor
        self.strenght = strenght
        self.mana = mana
        self. agility = agility
        self.level = level
        self.experience = experience

class Hero(Character):
    def __init__(self, name, hp_max, hp, magic_resist, armor, strenght, mana, agility, level, experience):
        super().__init__(name, hp_max, hp, magic_resist, armor, strenght, mana, agility, level, experience)
        self.inventory = []
        self.current_room = 0

    def __str__(self):
        return (f"Hero: {self.name}\n"
                f"HP: {self.hp}/{self.hp_max}\n"
                f"Magic Resist: {self.magic_resist}\n"
                f"Armor: {self.armor}\n"
                f"Strength: {self.strenght}\n"
                f"Mana: {self.mana}\n"
                f"Agility: {self.agility}\n"
                f"Level: {self.level}\n"
                f"Experience: {self.experience}\n"
                f"Inventory: {self.inventory}\n")
                
class Monster(Character):
    pass

class Ally(Character):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.resurrection_available = True # This is a superpower an ally has to protect the main character - The hero: player
    pass

class Room:
    def __init__(self, number, description):
        self.number = number
        self.description = description
        self.opponents = []  # list of monsters Hero can fight...
        self.items = []      # list of items Hero can collect...

    def enter(self, hero):
        print(f"\nYou enter Room {self.number}: {self.description}")
        # Later you can add: fight monsters, pick up items, etc.

# Lets create some def!
def select_door():
    doors = [1, 2, 3, 4, 5]
    while True:
        try:
            door_selected = int(input("Choose a door (1-5): "))
            if door_selected in doors:
                print(f"You are entering door {door_selected}...")
                return door_selected
            else:
                print("That door doesn't exist. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 5.")

# Lets create all 5 rooms!
rooms = {
    1: Room(1, "A quiet, dimly lit space. You feel a strange energy."),
    2: Room(2, "The air smells of smoke and danger."),
    3: Room(3, "The walls are lined with strange runes."),
    4: Room(4, "Cold and dark. You hear faint rattling."),
    5: Room(5, "Everything feels… unpredictable here."),
}

# Lets start the game!
print("<<<< Welcome to RPG - CLG >>>>") 


player = input(f"Please insert your name: ")

hero = Hero(player, 100, 100, 25, 25, 45, 45, 30, 1, 0 )

print(f"\nYor Character was created with the following stats:\n{hero}")

print("Welcome, adventurer!")
print("You stand before five mysterious doors.")
print("What awaits behind them? Only you will find out…")
print("Choose wisely, or fate may choose for you.\n")



hero.current_room = select_door()

while True:
    chosen_room = select_door(rooms)
    hero.current_room = chosen_room
    hero.current_room.enter(hero)
