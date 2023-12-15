from game.observer.observer import Observer
from game.observer.subject import Subject

class Bank(Subject, Observer):

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