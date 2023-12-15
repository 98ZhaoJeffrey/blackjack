from typing import List
from game.player import Player
from game.bank import Bank
from game.observer.observer import Observer
from game.observer.subject import Subject

class Game(Subject, Observer):
    # keep track of players
    # state of game
    players: List[Player] = []
    bank: Bank

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

    
    def play():
        pass

    def player_action():
        pass

    def dealer_action():
        pass

    def setup():
        pass


# set up the game: make player post bet, deal cards
# allow player action
# let banker make their action