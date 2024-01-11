import pytest
from math import ceil
from blackjack_game.deck import Deck

NUM_DECKS = 8
NUM_CARDS_DECK = 52
TOTAL_CARDS = NUM_DECKS * NUM_CARDS_DECK
SIXTY_PERCENT = ceil(0.6 * TOTAL_CARDS)


def test_deck_reset_valid():
    deck = Deck(number_decks=8)
    for _ in range(SIXTY_PERCENT):
        deck.deal()
    assert deck.should_reset_deck()

def test_deck_reset_invalid():
    deck = Deck(number_decks=8)
    for _ in range(SIXTY_PERCENT - 10):
        deck.deal()
    assert not deck.should_reset_deck()

def test_reset_deck():
    deck = Deck(number_decks=8)
    for _ in range(SIXTY_PERCENT):
        deck.deal()
    deck.reset()
    assert len(deck.deck) == TOTAL_CARDS