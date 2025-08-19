import random

class Card():
    """Standard card from 1 to 13!"""

    def __init__(self, kind:str, number:int):
        self.kind = kind
        self.number = number
    
    def __str__(self):
        return "%s of %s" % (self.number, self.kind)
    
class Gambler():
    '''BlackJack player'''
    def __init__(self,name,cards_in_hand,currently_sum):
        self.name = name
        self.cards_in_hand = cards_in_hand
        self.currently_sum = currently_sum
    def pick_card(self,card):
        cards.append(card)
    def get_initial_cards(self):
        for player in players:
            while len(player.cards_in_hand)<2:
                card = random.choice(cards)
                cards.remove(card)
                player.cards_in_hand.append(card)
    def show_initial_cards(self):
        for player in players:
            print(f"Cards for {player.name}:")
            print(f"{player.cards_in_hand[0]}")
            print(f"{player.cards_in_hand[1]}")
            player.total_sum()

    def total_sum(self):
        total_sum = 0
        for card in self.cards_in_hand:
            if card.number in ["Jack", "Queen", "King"]:
                value = 10
            elif card.number == "A":
                value = 11   # (we'll handle the 1/11 flexibility later)
            else:
                value = card.number
            total_sum += value
        return print(f"total sum: {total_sum}\n")
    
    def check_sum(self):
        if self.currently_sum < 21:
            print(f"{self.name} do you want another card?")


class Dealer(Gambler):
    '''NPC player'''
    def pick_hidden_card(self,card):
        hidden_card = card
        return hidden_card
    def sum(self):
        total_sum = self.pick_hidden_card.number + self.pick_hidden_card.number

kind_list = ["Spades","Hearts","Diamonds","Clubs"]
number_list = ["A",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]

cards = []

for kind in kind_list:
    for num in number_list:
        card = Card(kind, num)
        cards.append(card)

print("\n<<<< Welcome to Card - Game - Version: Blackjack >>>>") 
player = input(f"Please insert your name: ")

# Cards in hand
cards_user = []
cards_1 = []
cards_2 = []
cards_3 = []
cards_4 = []
cards_dealer = []

# Create player
user = Gambler(player,cards_user)
gambler_npc_1 = Gambler("Walter White",cards_1,0)
gambler_npc_2 = Gambler("Jesse Pinkman",cards_2,0)
gambler_npc_3 = Gambler("Saul Godman",cards_3,0)
gambler_npc_4 = Gambler("Tuco Salamanca",cards_4,0)
dealer = Dealer("Dealer - Badger",cards_dealer,0)

players = [gambler_npc_1,gambler_npc_2,gambler_npc_3,gambler_npc_4,dealer,user]

print(f"\nok {player}, rules are simple:")
print("- Get a hand value as close to 21 as possible without going over.") 
print("- Each player gets two cards face up on the table.") 
print("- There are 5 player, plus the dealer, whoever gets closer to 21 wins") 
print("- The dealer also gets two cards: one face up , and one face down.") 
print("- Players act one at a time, in your turn you can hit or stand, thats it.\n") 


user.get_initial_cards()
user.show_initial_cards()

print("ROUND 1") 

