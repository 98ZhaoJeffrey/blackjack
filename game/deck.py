from random import shuffle
from collections.abc import Callable
from collections import defaultdict 
from typing import List
from game.card import Card, Rank, Suit

class Deck:
    def __init__(self, deck_builder: Callable[[], List[Card]], number_decks: int = 1):
        self.number_decks = number_decks
        self._deck_builder = deck_builder
        self.deck = []
        self._used_cards = defaultdict(lambda: 0)

    def _build_deck(self):
        decks = [self._deck_builder() for _ in range(self.number_decks)]
        for deck in decks:
            self.deck += deck
        
    def shuffle(self):
        shuffle(self.deck)

    def deal(self, num_cards=1):
        dealt_cards = self.deck[:num_cards]
        for card in dealt_cards:
            self._used_cards[card] += 1
        self.deck[num_cards:]
        return dealt_cards

    def reset_deck(self):
        self.deck = self._build_deck()
        self._used_cards.clear() 
        self.shuffle()