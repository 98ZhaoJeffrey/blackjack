from typing import TYPE_CHECKING
from blackjack_game.split_rules.split_rules import SplitRule

if TYPE_CHECKING:
    from blackjack_game.hand import Hand

class Default_Split_Rule(SplitRule):
    def can_split_cards(self, hand: 'Hand') -> bool:
        """
        Checks if the hand can be split

        Args:
            hand (Hand): The hand we want to check if can split

        Returns:
            bool: Can we split this hand

        """
        return len(hand.cards) == 2 and hand.cards[0].rank == hand.cards[1].rank