from __future__ import annotations
from typing import  Dict, Optional, Protocol, Any

class Observer(Protocol):
    """
        The Observer interface declares the update method, used by subjects.
    """

    def update(self, subject: Subject, data: Dict[str, Any]) -> None:
        """
            Receive update from subject.
        """
        pass

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
