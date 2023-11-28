from dataclasses import dataclass
from typing import List
from functools import cached_property
from collections.abc import Callable
from enum import Enum

class Suit(Enum):
    SPADES = 'Spades'
    HEARTS = 'Hearts'
    CLUBS = 'Clubs'
    DIAMONDS = 'Diamonds'

class Rank(Enum):
    ACE = 'Ace'
    TWO = 'Two'
    THREE = 'Three'
    FOUR = 'Four'
    FIVE = 'Five'
    SIX = 'Six'
    SEVEN = 'Seven'
    EIGHT = 'Eight'
    NINE = 'Nine'
    TEN = 'Ten'
    JACK = 'Jack'
    QUEEN = 'Queen'
    KING = 'King'

def blackJackValueCalculator(rank: Rank) -> List[int]:
    '''
    Returns a list of all possible values that a rank can be

    Paramters:
        rank (Rank): Rank of the card
    
    Returns:
        value (List[int]): List of all possible values a rank can be 
    '''
    values = {
        Rank.ACE: [1, 11],
        Rank.TWO: [2],
        Rank.THREE: [3],
        Rank.FOUR: [4],
        Rank.FIVE: [5],
        Rank.SIX: [6],
        Rank.SEVEN: [7],
        Rank.EIGHT: [8],
        Rank.NINE: [9],
        Rank.TEN: [10],
        Rank.JACK: [10],
        Rank.QUEEN: [10],
        Rank.KING: [10],
    }
    value = values[rank: Rank]
    return value

@dataclass(forzen=True, eq=True)
class Card:
    '''
    Class to represent a card

    Args:
        rank (Rank): Rank of the card
        suit (Suit): Suit of the card
        rank_value_calculator (Callable[[Rank], List[int]]): Function that returns all possible values of a Rank 

    '''

    rank: Rank
    suit: Suit
    rank_value_calculator: Callable[[Rank], List[int]] # may move this to the game class

    @cached_property
    def rank_value(self):
        return self.rank_value_calculator(self.rank)
    
    def __str__(self):
        return 'f{self.rank} of f{self.suit}'