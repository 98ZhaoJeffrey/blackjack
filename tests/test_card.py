import pytest
from blackjack_game.card import Card, Rank, Suit


def test_number_card():
    card = Card(Rank.FIVE, Suit.DIAMONDS)
    assert card.rank_value[0] == 5

def test_face_card():
    card = Card(Rank.KING, Suit.HEARTS)
    assert card.rank_value[0] == 10

def test_ace_card():
    card = Card(Rank.ACE, Suit.SPADES)
    assert card.rank_value == [1, 11]