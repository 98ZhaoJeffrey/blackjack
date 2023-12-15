from typing import List, Protocol
from dataclasses import dataclass
from enum import Enum
from game.card import Card
from game.observer.observer import Observer
from game.observer.subject import Subject

class PlayerAction(Enum):
    HIT = 'Hit'
    STAND = 'Stand'
    SPLIT = 'Split'
    DOUBLE = 'DOUBLE'

@dataclass
class Player(Subject, Observer):
    name: str
    bankroll: int
    hand: List[List[Card]]
    bet: int

    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    def detach(self, observer: Observer) -> None:
        pass

    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass

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