from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from blackjack_game.hand import Hand

class SplitRule(Protocol):
    def can_split_cards(self, hand: 'Hand') -> bool:
        pass