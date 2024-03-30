from abc import abstractmethod, ABC
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from blackjack_game.hand import Hand
from blackjack_game.actions import PlayerAction
from blackjack_game.observer.observer_subject import Observer, Subject

@dataclass
class Player(Subject, ABC):
    name: str
    bankroll: int
    hands: List[Hand] = field(default_factory=list)
    bet: int = 0
    observers: List[Observer] = field(default_factory=list)

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
    
    @abstractmethod
    def make_action(self, actions: List[PlayerAction]) -> PlayerAction:
        """
            Ask player for action
        """
        pass