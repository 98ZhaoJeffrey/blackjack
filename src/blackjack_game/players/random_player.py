from typing import List
from blackjack_game.actions import PlayerAction
from random import choice
from dataclasses import dataclass, field
from blackjack_game.hand import Hand
from blackjack_game.observer.observer_subject import Observer
from blackjack_game.player import Player



@dataclass
class RandomPlayer(Player):
    def make_action(self, actions: List[PlayerAction]) -> PlayerAction:
        return choice(actions)