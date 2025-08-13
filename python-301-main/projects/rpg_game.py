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

print("<<<< Welcome to RPG - CLG >>>>") 
player = input(f"Please insert your name: ")

hero = Hero(player, 100, 100, 25, 25, 45, 45, 30, 1, 0 )

print(f"\nYor Character was created with the following stats:\n{hero}")

print("Welcome, adventurer!")
print("You stand before five mysterious doors.")
print("What awaits behind them? Only you will find out…")
print("Choose wisely, or fate may choose for you.\n")

print("Open one of the following doors:")
print("RED DOOR (enter: 1)")
print("YELLOW DOOR (enter: 2)")
print("WHITE DOOR (enter: 3)")
print("BLACK DOOR (enter: 4)")
print("PURPLE DOOR (enter: 5)")

door_select = input(" ")

