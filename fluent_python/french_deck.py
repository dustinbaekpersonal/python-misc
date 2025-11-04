"""French Deck."""
import random
from collections import namedtuple

# class Card:
#     """Class that stores trump card info."""
#     def __init__(self, rank: str, suit: str):
#         """Initialise."""
#         self.rank = rank
#         self.suit = suit
    
#     def __repr__(self):
#         """."""
#         return f"{self.__class__.__name__}(rank: {self.rank}, suit: {self.suit})"
    
Card = namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    """Class that stores trump cards."""

    ranks = list(range(2,11)) + list("JQKA")
    suits = {
        "spades": 3, 
        "hearts": 2,
        "diamonds": 1, 
        "clubs": 0 
    }

    def __init__(self):
        """Create combination of ranks and suits."""
        self._cards = [
            Card(rank, suit) for rank in self.ranks for suit in self.suits
        ]
    
    def __len__(self):
        """Total length of the deck."""
        return len(self._cards)
    
    def __getitem__(self, idx: int):
        """
        This makes the class iterable, indexing
        
        because it's iterable, `in` works and `for` works
        """
        return self._cards[idx]
    
    def ranking(self, card: Card):
        """Decide the rank of each card."""
        rank_value = self.ranks.index(card.rank)
        suit_value = self.suits[card.suit]
        return rank_value * len(self.suits) + suit_value

    
    def shuffle(self):
        """Shuffle the existing deck."""
        
        
    
if __name__ == "__main__":
    deck = FrenchDeck()
    