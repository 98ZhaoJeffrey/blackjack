import pytest
from blackjack_game.hand import Hand
from blackjack_game.actions import PlayerAction, generate_valid_player_actions
from blackjack_game.card import Card, Rank, Suit

def test_busted_hand():
    hand = Hand(cards=[Card(Rank.JACK, Suit.CLUBS), Card(Rank.JACK, Suit.CLUBS), Card(Rank.JACK, Suit.CLUBS)])
    hand.is_busted = True
    assert generate_valid_player_actions(hand) == []


def test_standing_hand():
    hand = Hand(cards=[Card(Rank.JACK, Suit.CLUBS), Card(Rank.JACK, Suit.CLUBS)])
    hand.is_standing = True
    assert generate_valid_player_actions(hand) == []

def test_doubled_hand():
    hand = Hand(cards=[Card(Rank.JACK, Suit.CLUBS), Card(Rank.JACK, Suit.CLUBS), Card(Rank.JACK, Suit.CLUBS)])
    hand.is_doubled = True
    assert generate_valid_player_actions(hand) == []

def test_split_hand():
    hand = Hand(cards=[Card(Rank.JACK, Suit.CLUBS), Card(Rank.JACK, Suit.CLUBS)])
    assert generate_valid_player_actions(hand) == [PlayerAction.DOUBLE, PlayerAction.HIT, PlayerAction.STAND, PlayerAction.SPLIT]

def test_normal_hand():
    hand = Hand(cards=[Card(Rank.JACK, Suit.CLUBS), Card(Rank.THREE, Suit.CLUBS), Card(Rank.JACK, Suit.CLUBS)])
    assert generate_valid_player_actions(hand) == [PlayerAction.DOUBLE, PlayerAction.HIT, PlayerAction.STAND]