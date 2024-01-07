from typing import List, Dict, Optional, Protocol, Any
from dataclasses import dataclass
from enum import Enum
from blackjack_game.hand import Hand
from blackjack_game.observer.observer import Observer
from blackjack_game.observer.subject import Subject

class PlayerAction(Enum):
    HIT = 'Hit'
    STAND = 'Stand'
    SPLIT = 'Split'
    DOUBLE = 'DOUBLE'

@dataclass
class Player(Subject, Protocol):
    name: str
    bankroll: int
    hands: List[Hand]
    bet: int
    observers: List[Observer]

    def attach(self, observer: Observer) -> None:
        """
            Attach an observer to the subject.
        """
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify(self, data: Dict[str, Any], observer: Optional[Observer]) -> None:
        """
            Notify observer
        """
        if(observer):
            observer.update(self, data)
        else:
            for obs in self.observers:
                obs.update(self, data)
    
    def modify_bankroll(self, value: int) -> None:
        self.bankroll += value

    def set_bet(self, bet: int) -> None:
        """
            Set bet size
        """
        self.bet = bet
    
    def make_action(self, actions: List[PlayerAction]) -> PlayerAction:
        """
            Ask player for action
        """
        pass