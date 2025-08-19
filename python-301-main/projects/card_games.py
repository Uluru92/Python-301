class Card():
    """Standard playing card from 1 to 13!"""

    def __init__(self, kind:str, number):
        self.kind = kind
        self.number = number
    
    def __str__(self):
        return "%s of %s" % (self.number, self.kind)
    
class Gambler():
    '''BlackJack player'''
    def __init__(self,name,cards_in_hand):
        self.name = name
        self.cards_in_hand = cards_in_hand
    def pick_card(self,card):
        cards.append(card)

class Dealer(Gambler):
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

for card in cards:
    print(card)

print("\n<<<< Welcome to Card - Game - Version: Blackjack >>>>") 
player = input(f"Please insert your name: ")

# Cards in hand
gambler_cards_in_hand = []
dealer_cards_in_hand = []

# Create player
user = Gambler(player,gambler_cards_in_hand)
dealer = Gambler("dealer_npc",dealer_cards_in_hand)
gambler_npc_1

print(f"\nok {player}, rules are simple:")
print("- Get a hand value as close to 21 as possible without going over.") 
print("- You play against the gambler_npc, whoever gets closer to 21 wins \n") 

while player_count < 22:
    