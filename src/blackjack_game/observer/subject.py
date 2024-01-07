from __future__ import annotations
from typing import Protocol, Optional, Dict, Any
from blackjack_game.observer.observer import Observer

class Subject(Protocol):
    """
        The Subject interface declares a set of methods for managing subscribers.
    """
    
    def attach(self, observer: Observer) -> None:
        """
            Attach an observer to the subject.
        """
        pass

    def detach(self, observer: Observer) -> None:
        """
            Detach an observer from the subject.
        """
        pass

    def notify(self, data: Dict[str, Any], observer: Optional[Observer]) -> None:
        """
            Notify an/all observer(s) about an event.
        """
        pass
