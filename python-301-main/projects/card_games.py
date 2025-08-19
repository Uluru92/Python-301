class Card():
    """Standard playing card from 1 to 13!"""

    def __init__(self, kind:str, number):
        self.kind = kind
        self.number = number
    
    def __str__(self):
        return "%s of %s" % (self.number, self.kind)
    
    def main(self):
        
        pass

kind_list = ["Spades","Hearts","Diamonds","Clubs"]
number_list = ["A",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]

cards = []

for kind in kind_list:
    for num in number_list:
        card = Card(kind, num)
        cards.append(card)

for card in cards:
    print(card)

