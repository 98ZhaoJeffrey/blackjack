from random import shuffle
from collections.abc import Callable
from collections import defaultdict 
from dataclasses import dataclass
from typing import List
from blackjack_game.blackjack_deck_generators.blackjack_deck_generator import BlackJack_Deck_Generator
from blackjack_game.card import Card, Rank, Suit
from blackjack_game.deck_generators.deck_generator import Deck_Generator

@dataclass
class Deck:    
    _deck_builder: Deck_Generator
    _blackjack_deck_builder: BlackJack_Deck_Generator
    number_decks: int = 1
    deck: List[Card] = []
    _total_cards: int = 0
    _used_cards: defaultdict[Card, int] = defaultdict(lambda: 0)
    RESET_DECK_PERCENTAGE: int = 60

    
    
    def __post_init__(self):
        self._build_blackjack_deck()

    def _build_blackjack_deck(self) -> None:
        """
        Builds a blackjack deck/shoe using the deck builder

        Args:
        
        Returns:

        """
        blackjack_deck = self._blackjack_deck_builder.generate_blackjack_deck(self._deck_builder, self.number_decks)
        self._total_cards = len(blackjack_deck)
        self.deck = blackjack_deck
        
    def _shuffle(self) -> None:
        """
        Shuffles the deck

        Args:

        Returns:

        """
        shuffle(self.deck)

    def deal(self) -> Card:
        """
        Deals a card from the deck

        Args:

        Returns:
            Card: The card was dealt from the deck
        
        """

        dealt_card = self.deck.pop()
        self._used_cards[dealt_card] += 1
        return dealt_card

    def reset_deck(self) -> None:
        """
        Resets the deck to a new deck

        Args:

        Returns:
        
        """
        self._build_blackjack_deck()
        self._used_cards.clear() 

    def should_reset_deck(self) -> bool:
        """
        Checks if we should reset the deck
        """
        return len(self.deck) * self.RESET_DECK_PERCENTAGE > len(self.deck)