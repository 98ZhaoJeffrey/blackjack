from __future__ import annotations
from typing import  Protocol
from subject import Subject

class Observer(Protocol):
    """
    The Observer interface declares the update method, used by subjects.
    """

    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass