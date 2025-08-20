'''Python Project: Card Game - Blackjack'''

import random
import time

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
    def get_another_card(self):
        """Decide if NPC wants another card (hit) or not (stand)."""
        score = self.total_sum() 
        if self.name == "Walter White":       # Smart/neutral strategy
            return score < 17
        elif self.name == "Jesse Pinkman":    # Risky
            return score < 19
        elif self.name == "Saul Godman":      # Conservative
            return score < 15
        elif self.name == "Tuco Salamanca":   # Crazy risk-taker
            return score < 20
        elif self.name.startswith("Dealer"):  # Dealer follows rules
            return score < 17
        else:  # Default
            return score < 17                 # Just in case we add more players

    def get_initial_cards(self):
        for player in players:
            while len(player.cards_in_hand)<2:
                card = random.choice(cards)
                cards.remove(card)
                player.cards_in_hand.append(card)
        time.sleep(1)
    def show_initial_cards(self):
        for player in players:
            if player.name == "Dealer - Badger":
                print(f"Cards for {player.name}:")
                print(f"Hidden card")
                print(f"{player.cards_in_hand[1]}")
                self.total_sum
                print(f"total sum: Secret\n")
            else:
                print(f"Cards for {player.name}:")
                print(f"{player.cards_in_hand[0]}")
                print(f"{player.cards_in_hand[1]}")
                print(f"total sum: {player.total_sum()}\n")
            time.sleep(1)

    def total_sum(self):
        total_sum = 0
        aces = 0

        for card in self.cards_in_hand:
            if card.number in ["Jack", "Queen", "King"]:
                value = 10
            elif card.number == "A":
                value = 11
                aces += 1   # (we'll handle the 1/11 flexibility later)
            else:
                value = card.number
            total_sum += value

        while total_sum > 21 and aces > 0:
            total_sum -= 10  # Count Ace as 1 instead of 11
            aces -= 1

        self.currently_sum = total_sum
        return self.currently_sum

def play():
    print("Let's play!")
    for player in players:
        if player.name != user.name:  # NPC turn
            while player.get_another_card():
                card = random.choice(cards)
                cards.remove(card)
                player.cards_in_hand.append(card)
                player.total_sum()
                print(f"{player.name} takes another card: {card}")
                

                if player.name != "Dealer - Badger":
                    print(f"New total: {player.currently_sum}")
                    time.sleep(1)
                else:
                    print("New total: Secret")  # hide dealer's total
                    time.sleep(1)

                if player.currently_sum > 21:
                    print(f"{player.name} busts!\n")
                    time.sleep(1)
                    break
                elif player.currently_sum == 21:
                    print(f"{player.name} got Blackjack!\n")
                    time.sleep(1)
                    break
            else:
                if player.name != "Dealer - Badger":
                    print(f"{player.name} stands with {player.currently_sum}\n")
                    time.sleep(1)
                else:
                    print(f"{player.name} stands with total: Secret\n")
                    time.sleep(1)

        if player.name == user.name:  # Human turn
             while True:
                print(f"\n{player.name}, your cards:")
                for card in player.cards_in_hand:
                    print(card)
                print(f"Current total: {player.total_sum()}")

                if player.currently_sum > 21:
                    print("You bust! Over 21 ❌")
                    break
                elif player.currently_sum == 21:
                    print("Blackjack! 🎉")
                    break

                choice = input("Do you want another card? (y/n): ").lower()
                if choice == "y":
                    card = random.choice(cards)
                    cards.remove(card)
                    player.cards_in_hand.append(card)
                    print(f"You drew: {card}")
                else:
                    print(f"You stand with {player.currently_sum}")
                    break

def announce_winner(players):
    # Filter out players who went higher than 21
    valid_players = [p for p in players if p.currently_sum <= 21]

    if not valid_players:
        print("\nNobody wins, everyone busted!")
        return

    # Find the best score
    best_score = max(p.currently_sum for p in valid_players)

    # Find all players who achieved it
    winners = [p for p in valid_players if p.currently_sum == best_score]

    print("\n===== FINAL RESULTS =====")
    for p in players:
        print(f"{p.name}: {p.currently_sum} ({'BUST' if p.currently_sum > 21 else ''})")

    print("\n🏆 Winner(s): " + ", ".join([w.name for w in winners]))
    print(f"With a score of {best_score}")

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
user = Gambler(player,cards_user,0)
gambler_npc_1 = Gambler("Walter White",cards_1,0)
gambler_npc_2 = Gambler("Jesse Pinkman",cards_2,0)
gambler_npc_3 = Gambler("Saul Godman",cards_3,0)
gambler_npc_4 = Gambler("Tuco Salamanca",cards_4,0)
dealer = Gambler("Dealer - Badger",cards_dealer,0)

players = [gambler_npc_1,gambler_npc_2,gambler_npc_3,gambler_npc_4,dealer,user]

print(f"\nok {player}, rules are simple:")
print("- Get a hand value as close to 21 as possible without going over.") 
print("- Each player gets two cards face up on the table.") 
print("- There are 5 player, plus the dealer, whoever gets closer to 21 wins") 
print("- The dealer also gets two cards: one face up , and one face down.") 
print("- Players act one at a time, in your turn you can hit or stand, thats it.\n") 

user.get_initial_cards()
user.show_initial_cards()
play()
announce_winner(players)