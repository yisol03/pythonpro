class Card:
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit

    def __str__(self):
        reply = self.rank + self.suit
        return reply

class Hand:
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
           reply = ""
           for card in self.cards:
               reply += str(card) + "  "
        else:
            reply = "<empty>"
        return reply

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """ A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards: # if len(self.cards) >  0
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards!")

deck1 = Deck()
print (deck1)  # <empty>

deck1.populate()
print (deck1)  # ordered deck

deck1.shuffle()
print (deck1)  # shuffled deck

my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand = 5)
print (my_hand)    # 5 alternating cards from deck
print (your_hand)  # 5 alternating cards from deck
print (deck1)      # deck minus first 10 cards	
deck1.clear()
print (deck1)     # <empty>


