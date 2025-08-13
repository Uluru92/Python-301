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
        pass

class Hero(Character):
    def __init__(self, name, hp_max, hp, magic_resist, armor, strenght, mana, agility, level, experience):
        super().__init__(name, hp_max, hp, magic_resist, armor, strenght, mana, agility, level, experience)
        self.inventory = []
    pass

class Monster(Character):
    pass

class Ally(Character):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.resurrection_available = True
    pass

