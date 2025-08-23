'''Python Project: Card Game - Blackjack

This is my improved version after Jon Fincher recommendations in discord:
https://discord.com/channels/947901271518634084/1407520880703307796/1407749539586113547

'''

import random
import time

class Card:
    """Standard card from 1 to 13!"""
    def __init__(self, kind:str, number:int):
        self.kind = kind
        self.number = number
    def __str__(self):
        return f"{self.number} of {self.kind}"
    
class Gambler:
    """Represents a single Blackjack player (human or NPC)."""
    def __init__(self, name, npc=False, dealer=False):
        self.name = name
        self.npc = npc
        self.dealer = dealer
        self.cards_in_hand = []
        self.currently_sum = 0

    def total_sum(self):
        """Compute total, handling Aces as 1 or 11."""
        total = 0
        aces = 0
        for card in self.cards_in_hand:
            if card.number in ["Jack", "Queen", "King"]:
                value = 10
            elif card.number == "A":
                value = 11
                aces += 1
            else:
                value = card.number
            total += value

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        self.currently_sum = total
        return self.currently_sum

    def wants_card(self):
        """Decide if NPC wants another card, or return None for human."""
        if self.npc or self.dealer:
            if self.dealer:
                return self.currently_sum < 17  # Dealer follows neutral rules
            # Example NPC strategies
            if self.name == "Walter White":     # Smart/neutral strategy
                return self.currently_sum < 17
            elif self.name == "Jesse Pinkman":  # Risky
                return self.currently_sum < 19
            elif self.name == "Saul Godman":    # Conservative
                return self.currently_sum < 15
            elif self.name == "Tuco Salamanca": # Crazy risk-taker
                return self.currently_sum < 20
            else:
                return self.currently_sum < 17  # Just in case we add more players
        else:
            return None  # Human decision handled externally

    def show_hand(self, hide_total=False, hide_first_card=False):
        """
        Display player's cards.
        """
        print(f"\n{self.name}'s cards:")
        for i, card in enumerate(self.cards_in_hand):
            # Hide first card only if flag is True AND it's the first card
            if hide_first_card and i == 0:
                print("Hidden card")
            else:
                print(card)
        if hide_total:
            print("Total: Secret")
        else:
            print(f"Total: {self.currently_sum}")

class Game:
    def __init__(self, players):
        self.players = players
        self.deck = self.create_deck()

    def create_deck(self):
        kinds = ["Spades","Hearts","Diamonds","Clubs"]
        numbers = ["A",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
        return [Card(kind, num) for kind in kinds for num in numbers]

    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players:
                card = random.choice(self.deck)
                self.deck.remove(card)
                player.cards_in_hand.append(card)
                player.total_sum()
                time.sleep(0.2)

    def show_initial_hands(self):
        print("\n===== Initial Hands =====")
        for player in self.players:
            if player.dealer:
                player.show_hand(hide_total=True, hide_first_card=True)
            else:
                player.show_hand()
            print()  # extra blank line
            time.sleep(1)

    def play_turns(self, user):
        for player in self.players:
            print("\n" + "-"*30)  # separator
            if player == user:
                self.human_turn(player)
            else:
                self.npc_turn(player)

    def npc_turn(self, player):
        if player.dealer:
            print(f"\n{player.name} will play their turn...")  # simple message
            while player.wants_card():
                card = random.choice(self.deck)
                self.deck.remove(card)
                player.cards_in_hand.append(card)
                player.total_sum()
                print(f"{player.name} draws a card")  # never show total
                time.sleep(1)
                if player.currently_sum >= 21:
                    break
            print(f"{player.name} stands with Secret\n")
        else:
            while player.wants_card():
                card = random.choice(self.deck)
                self.deck.remove(card)
                player.cards_in_hand.append(card)
                player.total_sum()
                print(f"\n{player.name} draws {card}")
                player.show_hand()  # show full NPC hand
                time.sleep(1)
                if player.currently_sum >= 21:
                    break
            if player.currently_sum <= 21:
                print(f"{player.name} stands with {player.currently_sum}\n")
    
    def human_turn(self, player):
        """Handle the human player's turn."""
        print(f"\n=== {player.name}'s Turn ===\n")
        while True:
            print("Your cards:")
            for card in player.cards_in_hand:
                print(card)
            print(f"Current total: {player.currently_sum}\n")

            if player.currently_sum > 21:
                print("You bust! Over 21 ❌\n")
                break
            elif player.currently_sum == 21:
                print("Blackjack! 🎉\n")
                break

            choice = input("Do you want another card? (y/n): ").lower()
            if choice == "y":
                card = random.choice(self.deck)
                self.deck.remove(card)
                player.cards_in_hand.append(card)
                player.total_sum()
                print(f"\nYou drew: {card}\n")
            else:
                print(f"You stand with {player.currently_sum}\n")
                break

    def announce_winner(self):
        valid = [p for p in self.players if p.currently_sum <= 21]
        if not valid:
            print("Everyone busted! No winner.")
            return
        best = max(p.currently_sum for p in valid)
        winners = [p.name for p in valid if p.currently_sum == best]
        print("\n===== FINAL RESULTS =====")
        for p in self.players:
            print(f"{p.name}: {p.currently_sum} ({'BUST' if p.currently_sum>21 else ''})")
        print("\n🏆 Winner(s): " + ", ".join(winners) + f" with {best}")

user_name = input("Enter your name: ")
user = Gambler(user_name)
npc1 = Gambler("Walter White", npc=True)
npc2 = Gambler("Jesse Pinkman", npc=True)
npc3 = Gambler("Saul Godman", npc=True)
npc4 = Gambler("Tuco Salamanca", npc=True)
dealer = Gambler("Dealer - Badger", dealer=True)

players = [npc1, npc2, npc3, npc4, dealer, user]

# Start game
game = Game(players)
game.deal_initial_cards()
game.show_initial_hands()
game.play_turns(user)
game.announce_winner()