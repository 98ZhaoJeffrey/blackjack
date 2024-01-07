from __future__ import annotations
from typing import  Dict, Protocol, Any
from blackjack_game.observer.subject import Subject

class Observer(Protocol):
    """
        The Observer interface declares the update method, used by subjects.
    """

    def update(self, subject: Subject, data: Dict[str, Any]) -> None:
        """
            Receive update from subject.
        """
        pass