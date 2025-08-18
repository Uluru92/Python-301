# Project RPG GAME! - Chapter 2:

# Lets create some classes!
import random

class Character:
    '''A base character... with this class, its born:
    The Hero - Main Character: Player
    The Monsters that need to be killed
    The Allies of the Hero as secondary chars
    Any other secondary character in the game...!'''

    def __init__(self, name:str, hp_max:int, hp:int, magic_resist:int, armor:int, strength: int, mana:int, agility:int, level:int, experience:int ):
        self.name = name
        self.hp_max = hp_max
        self.hp = hp
        self.magic_resist = magic_resist
        self.armor = armor
        self.strength = strength
        self.mana = mana
        self. agility = agility
        self.level = level
        self.experience = experience

class Monster(Character):
    pass    

class WeakOpponent(Monster):
    def attack(monster, hero):
        print(f"{hero.name} watch out! {monster.name} is about to attack you!")
        damage = hero.armor - monster.strength
        if damage > 0:
            print(f"{hero.name} has avoid the initial damage! Keep going, it's your turn to attack!")
        else:
            hero.hp += hero.hp + damage
            print(f"{hero.name} has taken {damage} damage points. Resulting with {hero.hp}/{hero.hp_max} HP.")
            hero.check_die()

class FinalBoss(Monster):
    def __init__(self, name, hp_max, hp, magic_resist, armor, strength, mana, agility, level, experience,Special_dmg):
        super().__init__(name, hp_max, hp, magic_resist, armor, strength, mana, agility, level, experience)
        self.Special_dmg = Special_dmg
    def attack(monster, hero):
        print(f"{hero.name} you are about to receive the a massive attack from {monster.name}")
        damage = hero.armor - monster.strength + hero.magic_resist - monster.mana - monster.Special_dmg
        if damage > 0:
            print(f"{hero.name} has avoid the initial damage!!! Nice move! Now focus on the fight, good luck!")
        else:
            hero.hp += hero.hp + damage
            print(f"{hero.name} has taken {damage} damage points. Resulting with {hero.hp}/{hero.hp_max} HP.")
            hero.check_die()

class Hero(Character):
    def __init__(self, name, hp_max, hp, magic_resist, armor, strength, mana, agility, level, experience):
        super().__init__(name, hp_max, hp, magic_resist, armor, strength, mana, agility, level, experience)
        self.inventory = []
        self.current_room = None
        self.depth_in_room = 0
        self.blessed = False

    def enter_room(self, room):
        self.current_room = room
        self.depth_in_room = 0 # reset depth every time the Hero enters a room
        print(f"\nNow you are inside the {room.name}")
        print(room.describe(self.depth_in_room))

        while True:
            # Special events depending on room & depth
            self.check_special_event()

            if self.depth_in_room + 1 < len(self.current_room.depths):
                choice = input("Do you want to go deeper? (y/n): ").strip().lower()
                if choice == "y":
                    self.depth_in_room += 1
                    print(self.current_room.describe(self.depth_in_room))
                elif choice == "n":
                    break
                else:
                    print("Please answer with 'y' or 'n'.")
            else:
                print("You can’t go deeper.")
                break

    def gain_experience(self, amount: int):
        """Add experience and level up if threshold is reached."""
        self.experience += amount
        print(f"You gained {amount} EXP! Total EXP: {self.experience}")
        
        # Example: every 100 EXP = 1 level
        while self.experience >= 100:
            self.experience -= 100
            self.level += 1
            self.hp_max += 70
            self.hp = self.hp_max # this way the Hero restores its HP to full max HP
            self.strength += 85
            self.agility += 85
            self.armor += 85
            print(f"🎉 Level up! You are now Level {self.level} and gained new stats:")
            print(hero)
    
    def check_special_event(self):
        # Room 1, depth 2 (index 1) Sword!
        if self.current_room.number == 1 and self.depth_in_room == 1:
            if "Sword" not in self.inventory:
                while True:  # Loop until valid input
                    choice = input("You see a sword on the floor. Pick it up? (y/n): ").strip().lower()
                    if choice in ["y", "n"]:
                        break
                    print("Invalid choice. Please type 'y' or 'n'.")

                if choice == "y":
                    self.inventory.append("Sword")
                    self.strength += 105  # Or whatever amount you want to increase
                    self.current_room.depths[self.depth_in_room] = "There is nothing else here."
                    self.current_room.depths[self.depth_in_room-1] = "There is nothing else here."
                    print(f"You picked up the Sword! Your strength increased! to {self.strength} points")
                else:
                    print("You leave the sword where it is.")
        # Room 1, depth 3 (index 2) Small Golem!
        if self.current_room.number == 1 and self.depth_in_room == 2:
            if not self.current_room.monster_defeated:
                while True:
                    print("A small golem appears from the shadows! ")
                    small_golem = WeakOpponent(name="Small Golem",hp_max=60,hp=60,magic_resist=15,armor=5,strength=5,mana=5,agility=0,level=1,experience=0)
                    print(f"Chances to win against {small_golem.name}: {round(hero.prob_to_win(small_golem)*100)}%")
                    choice = input("Fight or run? (fight/run): ").strip().lower()
                    if choice == "fight":
                        small_golem.attack(hero)
                        hero_won = hero.fight(small_golem)
                        if hero_won:
                            print("You defeated the small golem!")
                            self.current_room.depths[self.depth_in_room] = "There is nothing else here."
                            self.current_room.monster_defeated = True
                            # rewards
                            self.gain_experience(60)
                            self.hp += 45
                            self.hp_max += 45
                            self.strength += 45
                            self.agility += 45
                            self.magic_resist += 45
                            self.armor += 45
                            print(f"You gained 60 EXP, +45 HP, +45 Max HP, +45 Strength, +45 Agility, +45 Armor, +45 Magic Resist. New stats: \n{hero}")
                            return
                        else:
                            self.hp -= 25  # big penalty
                            print(f"The {small_golem.name} defeated you... You ended up with {self.hp}/{self.hp_max} HP")
                            self.check_die()
                            self.depth_in_room = 10
                            return  # exit the room

                    elif choice == "run":
                        print("You run back to the main room!")
                        return  # exit the room

                    else:
                        print("Invalid choice. Please type 'fight' or 'run'.")                     
        # Room 2, depth 1 (index 0) The air is thick and smoky, you lose hp just by entering this place
        if self.current_room.number == 2 and self.depth_in_room == 0:
            self.hp -= 5 # small penalty
            print(f"It's hard to breath here, you lost 5 hp. Your actual HP: {self.hp}/{self.hp_max}")
            self.check_die()
        # Room 2, depth 2 (index 1) You feel the heat intensify, you lose hp just by entering this place
        if self.current_room.number == 2 and self.depth_in_room == 1:
            self.hp -= 10 # medium penalty
            print(f"There are flames everywhere, you lost 10 hp. Your actual HP: {self.hp}/{self.hp_max}")
            self.check_die()
        # Room 2, depth 3 (index 2) Dragon apprears!
        if self.current_room.number == 2 and self.depth_in_room == 2:
            self.hp -= 15 # medium penalty
            print(f"You got paralized for a moment just by the Dragon staring at you, you lost 15 hp. Your actual HP: {self.hp}/{self.hp_max}")
            self.check_die()
            if not self.current_room.monster_defeated:
                while True: 
                    print("The Dragon Raid Boss appears from the flames!")
                    dragon = FinalBoss(name="Dragon Raid Boss",hp_max=250,hp=250,magic_resist=65,armor=85,strength=70,mana=70,agility=40,level=5,experience=0,Special_dmg=65)
                    print(f"Chances to win against {dragon.name}: {round(hero.prob_to_win(dragon)*100)}%")
                    choice = input("Fight or run? (fight/run): ").strip().lower()
                    if choice == "fight":
                        dragon.attack(hero)
                        hero_won = hero.fight(dragon)
                        if hero_won:
                            print("🎉 Congratulations! You defeated the Dragon and finished the game! 🎉")
                            exit()  # stops the game
                        else:
                            self.hp -= 70  # big penalty
                            print(f"The {dragon.name} defeated you... You ended up with {self.hp}/{self.hp_max} HP")
                            self.check_die()
                            self.depth_in_room = 10
                            return  # exit the room
                    elif choice == "run":
                        print("You run back to the main room!")
                        return  # exit the room
                    else:
                        print("Invalid choice. Please type 'fight' or 'run'.")
        # Room 3, depth 1 (index 0) Priest appears!
        if self.current_room.number == 3 and self.depth_in_room == 0:
            if not self.current_room.ally_appears:
                while True:
                    choice = input("If you kneel, you receive the blessing of the Gods! knee or stand? (kneel/stand): ").strip().lower()
                    if choice == "kneel":
                        self.current_room.depths[self.depth_in_room] = "There is nothing here... seems like the priest left"
                        self.current_room.ally_appears = True
                        self.blessed = True
                        print(f"{self.name} was blessed with the power of resurrection! You can come from Death once!")
                        return
                    elif choice == "stand":
                        self.current_room.depths[self.depth_in_room] = "There is nothing here... seems like the priest left"
                        self.current_room.ally_appears = True
                        print(f"{self.name}, you rejected the bless of the Gods... Good luck! *Priest desappears*")
                        return
                    else:
                        print("Invalid choice. Please type 'fight' or 'run'.")
        # Room 3, depth 2 (index 1) Mana Potion!
        if self.current_room.number == 3 and self.depth_in_room == 1:
            if "Mana Potion" not in self.inventory:
                while True:
                    choice = input("You found a Mana Potion! Pick it up? (y/n): ").strip().lower()
                    if choice in ["y", "n"]:
                        break
                    print("Invalid choice. Please type 'y' or 'n'.")

                if choice == "y":
                    self.inventory.append("Mana Potion")
                    self.mana += 85
                    self.current_room.depths[self.depth_in_room] = "There is nothing else here."
                    print(f"You picked up the Mana Potion! Your mana increased to {self.mana} points!")
                else:
                    print("You leave the Mana Potion where it is.") 
        # Room 3, depth 3 (index 2) Wizzard Hat
        if self.current_room.number == 3 and self.depth_in_room == 2:
            if "Wizzard Hat" not in self.inventory:
                while True:
                    choice = input("You found a Wizzard Hat! Pick it up? (y/n): ").strip().lower()
                    if choice in ["y", "n"]:
                        break
                    print("Invalid choice. Please type 'y' or 'n'.")

                if choice == "y":
                    self.inventory.append("Wizzard Hat")
                    self.magic_resist += 95
                    self.current_room.depths[self.depth_in_room] = "There is nothing else here."
                    print(f"You picked up the Wizzard Hat! Your magic resist increased to {self.magic_resist} points!")
                else:
                    print("You leave the Mana Potion where it is.") 
        # Room 4, depth 2 (index 1) Chain Armor!
        if self.current_room.number == 4 and self.depth_in_room == 1:
            if "Chain Armor" not in self.inventory:
                while True:  
                    choice = input("You see a chain armor on the floor. Pick it up? (y/n): ").strip().lower()
                    if choice in ["y", "n"]:
                        break
                    print("Invalid choice. Please type 'y' or 'n'.")

                if choice == "y":
                    self.inventory.append("Chain Armor")
                    self.armor += 90
                    self.current_room.depths[self.depth_in_room] = "There is nothing else here."
                    print(f"You picked up the Chain Armor! Your Armor increased! to {self.armor} points")
                else:
                    print("You leave the chain armor where it is.")
        # Room 4, depth 3 (index 2) Skeleton monster!
        if self.current_room.number == 4 and self.depth_in_room == 2:
            if not self.current_room.monster_defeated:
                while True:
                    print("A Skeleton forms from the floor bones!")
                    skeleton = WeakOpponent(name="Skeleton",hp_max=80,hp=80,magic_resist=25,armor=25,strength=40,mana=5,agility=15,level=3,experience=0)
                    print(f"Chances to win against {skeleton.name}: {round(hero.prob_to_win(skeleton)*100)}%")
                    choice = input("Fight or run? (fight/run): ").strip().lower()
                    if choice == "fight":
                        skeleton.attack(hero)
                        hero_won = hero.fight(skeleton)
                        if hero_won:
                            print("You defeated the Skeleton!")
                            self.current_room.depths[self.depth_in_room] = "There is nothing else here."
                            self.current_room.monster_defeated = True
                            # rewards
                            self.gain_experience(90)
                            self.hp_max += 65
                            self.hp += 65
                            self.magic_resist += 65
                            self.strength += 65
                            self.agility += 65
                            self.armor += 65
                            print(f"From killing the {skeleton.name}, you gained +65 HP, +65 Max HP, 65 Strength, +65 Agility, +65 Armor, +65 Magic Resist. New stats:\n{hero}")
                            return
                        else:
                            self.hp -= 55  # medium penalty
                            print(f"The {skeleton.name} defeated you... You ended up with {self.hp}/{self.hp_max} HP")
                            self.check_die()
                            self.depth_in_room = 10
                            return  # exit the room
                    elif choice == "run":
                        print("You run back to the main room!")
                        return  # exit the room
                    else:
                        print("Invalid choice. Please type 'fight' or 'run'.")   
        # Room 5, depth 1 (index 0) Random room - you get teleported to anyother...!
        if self.current_room.number == 5 and self.depth_in_room == 0:
            random_room = random.choice(rooms[:4])  # pick a random room (1-4)
            print(f"\n***...The room shifts! You are teleported to another place...***")
            self.current_room = random_room
            self.depth_in_room = 0
            print(f"\nNow you are inside the {random_room.name}")
            print(random_room.describe(self.depth_in_room))
            return

    def prob_to_win(self, monster: Monster):
        '''Calculate and show the probability to win agains the monster in front of you'''
        # Calculate win probability based on attributes
        hero_score = (self.strength*0.2+self.agility*0.15+self.mana*0.15+self.hp*0.3+self.armor*0.1+self.magic_resist*0.1)
        monster_score = (monster.strength*0.2+monster.agility*0.15+monster.mana*0.15+monster.hp*0.3+monster.armor*0.1+monster.magic_resist*0.1)
        # Calculate probability of winning
        win_probability = hero_score / (hero_score + monster_score)
        return win_probability

    def fight(self, monster: Monster) -> bool:
        """Generic fight against any Monster. Returns True if hero wins, False if hero loses."""
        win_probability = self.prob_to_win(monster)
        if random.random() < win_probability:
            return True
        else:
            return False

    def check_die (self):
        if self.hp <= 0:
            if self.blessed == True:
                self.hp = 50
                self.hp_max = 100
                print(f"{self.name}, you were revived by the bless of the Gods with {self.hp}/{self.hp_max} HP")
                return
            else:
                print("You lost the game!")
                exit()  # stops the game

    def go_deeper(self):
        if self.current_room and self.depth_in_room + 1 < len(self.current_room.depths):
            self.depth_in_room += 1
            print(self.current_room.describe(self.depth_in_room))
        else:
            print("You can’t go deeper.")

    def __str__(self):
        return (f"Hero: {self.name}\n"
                f"HP: {self.hp}/{self.hp_max}\n"
                f"Magic Resist: {self.magic_resist}\n"
                f"Armor: {self.armor}\n"
                f"Strength: {self.strength}\n"
                f"Mana: {self.mana}\n"
                f"Agility: {self.agility}\n"
                f"Level: {self.level}\n"
                f"Experience: {self.experience}\n"
                f"Inventory: {self.inventory}\n")

class Room:
    def __init__(self, number, name, depths):
        self.number = number            # Door number
        self.name = name                # Room title
        self.depths = depths            # List of strings for each depth
        self.opponents = []             # Monsters in the room
        self.items = []                 # Items in the room
        self.monster_defeated = False   # flag for the room's monster
        self.ally_appears = False       # flag for the room's ally

    def describe(self, depth):
        if depth < len(self.depths):
            return f"You are at depth {depth + 1}: {self.depths[depth]}"
        else:
            return "You can’t go deeper."

# Lets create some def!
def select_door():
    while True:
        try:
            door_selected = int(input("You are in the Main Room, choose a door (1-5): "))
            if 1 <= door_selected <= 5:
                print(f"You are entering door {door_selected}...")
                return rooms[door_selected - 1]  # return the actual Room
            else:
                print("That door doesn't exist. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 5.")

# Lets create all 5 rooms!
rooms = [
    Room(1, "Empty Room", depths=["Seems like there is nothing here... wait... something shines in the deep shadows...","Deeper in, you notice something glinting on the floor. It is a sword!","A small creature suddenly appears from the shadows."]),
    Room(2, "Dragon Room", depths=["The air is thick and smoky, and a low growl echoes.","You feel the heat intensify; something massive is nearby.","The ultimate foe reveals itself, eyes burning with fury."]),
    Room(3, "Priest Room", depths=["Soft light filters through stained glass; the priest greets you. He asks if you wish to receive his blessing. (You must kneel to accept it.)","You notice a glowing mana potion on a small altar.","A mystical wizard hat rests on a pedestal, radiating magic."]),
    Room(4, "Skeleton Room", depths=["The room is dark and littered with bones on the floor. Nothing to pick up here.","A chain armor lies hidden beneath the bones, waiting to be claimed.","A small skeleton monster stirs, ready to attack."]),
    Room(5, "Random Room", depths=["The room feels unstable; as soon as you step in, the walls shift and you are teleported to another random room."])
]

# Lets start the game!
print("<<<< Welcome to RPG - CLG >>>>") 

player = input(f"Please insert your name: ")

hero = Hero(player, 100, 100, 25, 25, 45, 45, 30, 1, 0 )

print(f"\nYor Character was created with the following stats:\n{hero}")

print("Welcome, adventurer!")
print("You stand before five mysterious doors.")
print("What awaits behind them? Only you will find out…")
print("Choose wisely, or fate may choose for you.\n")


while hero.hp != 0:
    hero.current_room = select_door()
    chosen_room = hero.current_room
    hero.enter_room(chosen_room)


