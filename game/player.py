from typing import List# Protocol
from dataclasses import dataclass
from enum import Enum
from game.card import Card

class PlayerAction(Enum):
    HIT = 'Hit'
    STAND = 'Stand'
    SPLIT = 'Split'
    DOUBLE = 'DOUBLE'

@dataclass
class Player:
    name: str
    bankroll: int
    hand: List[Card]
    bet: int

    def bet(self) -> None:
        # bet money for the current hand
        # update the game what the bet is
        pass

    def action(self) -> None:
        # update the game what the player action is
        pass

    # Player needs to be able to do many actions
    # Hit -> get a card
    # Stand stop getting cards
    # Split the cards
    # Double down 2x the bet and get 1 extra card
    # Player should get actions from an observer and emit events