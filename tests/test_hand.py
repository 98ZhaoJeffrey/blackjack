import pytest
from blackjack_game.hand import Hand
from blackjack_game.card import Card, Rank, Suit
from blackjack_game.exceptions.HandSplitException import HandSplitException

@pytest.mark.parametrize("no_aces_no_busted,expected", [
    ([Card(Rank.EIGHT, Suit.DIAMONDS), Card(Rank.TWO, Suit.SPADES)], [10]),
    ([Card(Rank.JACK, Suit.DIAMONDS)], [10]),
    ([Card(Rank.TWO, Suit.DIAMONDS), Card(Rank.TWO, Suit.DIAMONDS), Card(Rank.TWO, Suit.DIAMONDS), Card(Rank.TWO, Suit.DIAMONDS)], [8]),
    ([Card(Rank.KING, Suit.CLUBS), Card(Rank.THREE, Suit.HEARTS), Card(Rank.FIVE, Suit.CLUBS), Card(Rank.TWO, Suit.DIAMONDS)], [20]),
    ([Card(Rank.THREE, Suit.DIAMONDS), Card(Rank.TWO, Suit.DIAMONDS), Card(Rank.TWO, Suit.DIAMONDS), Card(Rank.TWO, Suit.DIAMONDS)], [9]),
    ([Card(Rank.JACK, Suit.DIAMONDS), Card(Rank.TEN, Suit.DIAMONDS)], [20]),
    ([Card(Rank.TWO, Suit.DIAMONDS), Card(Rank.THREE, Suit.CLUBS), Card(Rank.FOUR, Suit.SPADES), Card(Rank.FIVE, Suit.SPADES), Card(Rank.SIX, Suit.HEARTS)], [20])
])
def test_hand_no_ace_no_busted(no_aces_no_busted, expected):
    assert(Hand(no_aces_no_busted).get_valid_hand_values()) == expected


@pytest.mark.parametrize("busted,expected", [
    ([Card(Rank.JACK, Suit.DIAMONDS), Card(Rank.QUEEN, Suit.DIAMONDS), Card(Rank.KING, Suit.SPADES)], []),
    ([Card(Rank.JACK, Suit.DIAMONDS), Card(Rank.EIGHT, Suit.DIAMONDS), Card(Rank.EIGHT, Suit.DIAMONDS)], []),
    ([Card(Rank.KING, Suit.CLUBS), Card(Rank.THREE, Suit.HEARTS), Card(Rank.FIVE, Suit.CLUBS), Card(Rank.SEVEN, Suit.DIAMONDS)], []),
    ([Card(Rank.TEN, Suit.DIAMONDS), Card(Rank.TEN, Suit.DIAMONDS), Card(Rank.TWO, Suit.DIAMONDS), Card(Rank.TWO, Suit.DIAMONDS)], []),
    ([Card(Rank.JACK, Suit.DIAMONDS), Card(Rank.TEN, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS)], []),
    ([Card(Rank.THREE, Suit.DIAMONDS), Card(Rank.FOUR, Suit.CLUBS), Card(Rank.FOUR, Suit.SPADES), Card(Rank.FIVE, Suit.SPADES), Card(Rank.SIX, Suit.HEARTS)], [])
])
def test_hand_busted(busted, expected):
    assert(Hand(busted).get_valid_hand_values()) == expected

@pytest.mark.parametrize("not_busted_with_ace,expected", [
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.QUEEN, Suit.DIAMONDS)], [11, 21]),
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.EIGHT, Suit.DIAMONDS), Card(Rank.EIGHT, Suit.DIAMONDS)], [17]),
    ([Card(Rank.KING, Suit.CLUBS), Card(Rank.ACE, Suit.HEARTS), Card(Rank.FIVE, Suit.CLUBS)], [16]),
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.TEN, Suit.DIAMONDS), Card(Rank.TEN, Suit.DIAMONDS)], [21]),
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS)], [4, 14]),
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.TWO, Suit.CLUBS), Card(Rank.THREE, Suit.HEARTS), Card(Rank.FOUR, Suit.SPADES), Card(Rank.FIVE, Suit.SPADES), ], [15]),
    ([Card(Rank.FIVE, Suit.CLUBS), Card(Rank.ACE, Suit.HEARTS), Card(Rank.FIVE, Suit.CLUBS)], [11, 21]),
])
def test_hand_not_busted_with_ace(not_busted_with_ace, expected):
    assert (Hand(not_busted_with_ace).get_valid_hand_values()) == expected


@pytest.mark.parametrize("multiple_aces,expected", [
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.EIGHT, Suit.DIAMONDS)], [10, 20]),
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.JACK, Suit.DIAMONDS)], [12]),
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS)], [2, 12]),
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.DIAMONDS)], [4, 14]),
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.TWO, Suit.CLUBS), Card(Rank.THREE, Suit.HEARTS), Card(Rank.FOUR, Suit.SPADES), Card(Rank.FIVE, Suit.SPADES), ], [15]),
    ([Card(Rank.ACE, Suit.CLUBS), Card(Rank.ACE, Suit.HEARTS), Card(Rank.QUEEN, Suit.CLUBS), Card(Rank.KING, Suit.CLUBS)], []),
])
def test_hand_multiple_aces(multiple_aces, expected):
    assert (Hand(multiple_aces).get_valid_hand_values()) == expected

@pytest.mark.xfail
@pytest.mark.parametrize("valid_splits,expected", [
    ([Card(Rank.ACE, Suit.DIAMONDS), Card(Rank.ACE, Suit.CLUBS)], [Card(Rank.ACE, Suit.CLUBS)]),
    ([Card(Rank.THREE, Suit.HEARTS), Card(Rank.THREE, Suit.DIAMONDS)], [Card(Rank.THREE, Suit.DIAMONDS)]),
    ([Card(Rank.KING, Suit.DIAMONDS), Card(Rank.KING, Suit.SPADES)], [Card(Rank.KING, Suit.SPADES)]),
    ([Card(Rank.FIVE, Suit.DIAMONDS), Card(Rank.FIVE, Suit.DIAMONDS)], [Card(Rank.FIVE, Suit.DIAMONDS)]),
])
def test_split_hand(valid_splits, expected):
    result = Hand(valid_splits).split()
    assert result == expected

def test_invalid_split():
    with pytest.raises(HandSplitException):
        Hand([Card(Rank.TWO, Suit.DIAMONDS), Card(Rank.ACE, Suit.CLUBS)]).split()

def test_invalid_split_face_card():
    with pytest.raises(HandSplitException):
        Hand([Card(Rank.KING, Suit.DIAMONDS), Card(Rank.QUEEN, Suit.CLUBS)]).split()

def test_invalid_split_wrong_length():
    with pytest.raises(HandSplitException):
        Hand([Card(Rank.KING, Suit.DIAMONDS), Card(Rank.KING, Suit.CLUBS), Card(Rank.KING, Suit.CLUBS)]).split()
