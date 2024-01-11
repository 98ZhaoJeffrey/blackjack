from __future__ import annotations
from typing import List, TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from blackjack_game.hand import Hand

class PlayerAction(Enum):
    HIT = 'Hit'
    STAND = 'Stand'
    SPLIT = 'Split'
    DOUBLE = 'DOUBLE'

def generate_valid_player_actions(hand: 'Hand') -> List[PlayerAction]:
    """
    Generate all possible actions possible from a given hand

    Args:
        hand (Hand): The hand we want the possible actions from

    Returns:
        List[PlayerAction]: Every possible action that can be taken from the hand

    """
    turn_ended = hand.is_standing or hand.is_doubled or hand.is_busted
    can_split = hand.split_rule.can_split_cards(hand)
    if(turn_ended):
        return []
    if(can_split):
        return [PlayerAction.DOUBLE, PlayerAction.HIT, PlayerAction.STAND, PlayerAction.SPLIT]
    else:
        return [PlayerAction.DOUBLE, PlayerAction.HIT, PlayerAction.STAND]
