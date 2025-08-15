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

class Hero(Character):
    def __init__(self, name, hp_max, hp, magic_resist, armor, strength, mana, agility, level, experience):
        super().__init__(name, hp_max, hp, magic_resist, armor, strength, mana, agility, level, experience)
        self.inventory = []
        self.current_room = None
        self.depth_in_room = 0

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
            self.hp_max += 10  # optional: increase stats on level up
            self.hp = self.hp_max
            self.strength += 2
            self.agility += 2
            self.armor += 1
            print(f"🎉 Level up! You are now Level {self.level}!")
    
    def check_special_event(self):
        # Room 1, depth 2 (index 1) has a sword
        if self.current_room.number == 1 and self.depth_in_room == 1:
            if "Sword" not in self.inventory:
                while True:  # Loop until valid input
                    choice = input("You see a sword on the floor. Pick it up? (y/n): ").strip().lower()
                    if choice in ["y", "n"]:
                        break
                    print("Invalid choice. Please type 'y' or 'n'.")

                if choice == "y":
                    self.inventory.append("Sword")
                    self.strength += 35  # Or whatever amount you want to increase
                    self.current_room.depths[self.depth_in_room] = "You are at depth 2: There is nothing else here."
                    self.current_room.depths[self.depth_in_room-1] = "You are at depth 1: There is nothing here."
                    print("You picked up the Sword! Your strength increased!")
                else:
                    print("You leave the sword where it is.")
        # Room 1, depth 3 (index 2) has a mosnter (small golem)
        if self.current_room.number == 1 and self.depth_in_room == 2:
            if not self.current_room.monster_defeated:
                while True:  # loop until valid input
                    choice = input("A small golem appears from the shadows! Fight or run? (fight/run): ").strip().lower()
                    if choice == "fight":
                        # Create the monster
                        small_golem = Monster(
                            name="Small Golem",
                            hp_max=60,
                            hp=60,
                            magic_resist=15,
                            armor=25,
                            strength=20,
                            mana=0,
                            agility=2,
                            level=1,
                            experience=0
                        )
                        
                        # Calculate win probability
                        hero_score = self.hp + self.strength + self.agility + self.mana + self.armor + self.magic_resist
                        monster_score = small_golem.hp + small_golem.strength + small_golem.agility + small_golem.mana + small_golem.armor + small_golem.magic_resist
                        probability = hero_score / (hero_score + monster_score)
                        
                        print(f"Probability to win: {round(probability*100)}%")
                        
                        # Decide outcome randomly
                        if random.random() < probability:
                            print("You defeated the small golem!")
                            self.current_room.depths[self.depth_in_room] = "You are at depth 3: There is nothing else here."
                            self.current_room.monster_defeated = True
                            # rewards
                            self.gain_experience(60)
                            self.hp_max += 5
                            self.strength += 2
                            self.agility += 2
                            self.armor += 1  # gloves
                            print("You gained 10 EXP, +5 Max HP, +2 Strength, +2 Agility, +1 Armor (gloves)")
                            # potion added to inventory
                            self.inventory.append("HP Potion")
                            print("You found a HP Potion!")
                            return
                        else:
                            print("The small golem defeated you! You retreat to the main room.")
                            self.hp -= 30  # small penalty
                            self.depth_in_room = 10
                            return

                    elif choice == "run":
                        print("You run back to the main room!")
                        return  # exit the room

                    else:
                        print("Invalid choice. Please type 'fight' or 'run'.")
        # Room 2, depth 1 (index 0) The air is thick and smoky, you lose hp just by entering this place
        if self.current_room.number == 2 and self.depth_in_room == 0:
            self.hp -= 5 # small penalty
            print(f"It's hard to breath here, you lost 5 hp. Your actual HP: {self.hp}/{self.hp_max}")
        # Room 2, depth 2 (index 1) You feel the heat intensify, you lose hp just by entering this place
        if self.current_room.number == 2 and self.depth_in_room == 1:
            self.hp -= 10 # medium penalty
            print(f"There are flames everywhere, you lost 10 hp. Your actual HP: {self.hp}/{self.hp_max}")
        # Room 2, depth 3 (index 2) Dragon apprears!
        if self.current_room.number == 2 and self.depth_in_room == 2:
            self.hp -= 15 # medium penalty
            print(f"You got paralized for a moment just by the Dragon staring at you, you lost 15 hp. Your actual HP: {self.hp}/{self.hp_max}")

            if not self.current_room.monster_defeated:
                while True:  # loop until valid input
                    choice = input("A small golem appears from the shadows! Fight or run? (fight/run): ").strip().lower()
                    if choice == "fight":
                        # Create the monster
                        dragon = Monster(
                            name="Dragon Raid Boss",
                            hp_max=120,
                            hp=120,
                            magic_resist=70,
                            armor=90,
                            strength=110,
                            mana=70,
                            agility=0,
                            level=25,
                            experience=0
                        )
                        
                        hero_won = hero.fight(dragon)
                        if hero_won:
                            print("🎉 Congratulations! You defeated the Dragon and finished the game! 🎉")
                            exit()  # stops the game
                        else:
                            self.hp -= 65  # big penalty
                            print(f"The {dragon.name} defeated you... You ended up with {self.hp}/{self.hp_max} HP")
                            self.depth_in_room = 10
                            return  # exit the room

                    elif choice == "run":
                        print("You run back to the main room!")
                        return  # exit the room

                    else:
                        print("Invalid choice. Please type 'fight' or 'run'.")

    def fight(self, monster: Monster) -> bool:
        """Generic fight against any Monster. Returns True if hero wins, False if hero loses."""
        # Calculate win probability based on attributes
        hero_score = (
            self.strength * 0.3 +
            self.agility * 0.2 +
            self.mana * 0.1 +
            self.hp_max * 0.2 +
            self.armor * 0.1 +
            self.magic_resist * 0.1
        )
        monster_score = (
            monster.strength * 0.3 +
            monster.agility * 0.2 +
            monster.mana * 0.1 +
            monster.hp_max * 0.2 +
            monster.armor * 0.1 +
            monster.magic_resist * 0.1
        )

        # Calculate probability of winning
        win_probability = hero_score / (hero_score + monster_score)
        print(f"Chance to win against {monster.name}: {round(win_probability * 100)}%")

        # Determine fight outcome randomly based on probability
        if random.random() < win_probability:
            return True
        else:
            return False

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
                


class Ally(Character):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.resurrection_available = True # This is a superpower an ally has to protect the main character - The hero: player
    pass

class Room:
    def __init__(self, number, name, depths):
        self.number = number         # Door number
        self.name = name             # Room title
        self.depths = depths         # List of strings for each depth
        self.opponents = []          # Monsters in the room
        self.items = []              # Items in the room
        self.monster_defeated = False  # flag for the room's monster

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


