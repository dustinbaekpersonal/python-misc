from collections import namedtuple
from random import choice

Card = namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + ["A", "J", "Q", "K"]
    suits = "diamonds spades hearts clubs".split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in FrenchDeck.ranks for suit in FrenchDeck.suits]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
    deck = FrenchDeck()
    print(deck._cards)

    print(len(deck))
    
    print(id(deck))
    print(id(FrenchDeck))
    print(id(FrenchDeck))
    print(id(FrenchDeck()))
    
    print(deck[0])