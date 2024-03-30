from typing import List
from blackjack_game.actions import PlayerAction
from dataclasses import dataclass, field
from blackjack_game.hand import Hand
from blackjack_game.observer.observer_subject import Observer
from blackjack_game.player import Player


@dataclass
class TerminalPlayer(Player):
    def make_action(self, actions: List[PlayerAction]) -> PlayerAction:        
        selected_action = input(f"Pick an action: {[f'{act.value}' for act in actions]}: ").lower()
        return next(filter(lambda x: x.value.lower() == selected_action, actions))