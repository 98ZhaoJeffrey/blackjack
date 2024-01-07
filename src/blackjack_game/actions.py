from typing import List
from blackjack_game.hand import Hand
from blackjack_game.player import PlayerAction

def default_split_rule(hand: Hand) -> bool:
    """
    Checks if the hand can be split

    Args:
        hand (Hand): The hand we want to check if can split

    Returns:
        bool: Can we split this hand

    """
    return len(hand.cards) == 2 and hand.cards[0].rank == hand.cards[1].rank

def generate_valid_player_actions(hand: Hand) -> List[PlayerAction]:
    """
    Generate all possible actions possible from a given hand

    Args:
        hand (Hand): The hand we want the possible actions from

    Returns:
        List[PlayerAction]: Every possible action that can be taken from the hand

    """
    turn_ended = hand.is_standing or hand.is_doubled or hand.is_busted
    can_split = default_split_rule(hand)
    if(turn_ended):
        return []
    if(can_split):
        return [PlayerAction.DOUBLE, PlayerAction.HIT, PlayerAction.STAND, PlayerAction.SPLIT]
    else:
        return [PlayerAction.DOUBLE, PlayerAction.HIT, PlayerAction.STAND]
