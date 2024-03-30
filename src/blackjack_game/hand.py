from .card import Card, Rank
from typing import List, Dict, Optional, Protocol
from dataclasses import dataclass, field
from .exceptions.HandSplitException import HandSplitException
from blackjack_game.split_rules.default_split_rules import Default_Split_Rule
from blackjack_game.split_rules.split_rules import SplitRule

@dataclass
class Hand():
    
    cards: List[Card] = field(default_factory=list)
    is_standing: bool = False
    is_doubled: bool = False
    is_busted: bool = False
    split_rule: SplitRule = Default_Split_Rule()

    def __repr__(self) -> str:
        return f'{[str(card) for card in self.cards]}'

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def split(self) -> Card:
        """
        Splits the hand

        Args:

        Returns:
            Card: The card that is split into the new hand
        """
        can_split_cards = self.split_rule.can_split_cards(self) 
        if(can_split_cards):
            return self.cards.pop()
        else:
            raise HandSplitException(f"Can't split {[card for card in self.cards]}")
    
    def get_valid_hand_values(self) -> List[int]:
        """
        Generates all possible hand values without busting

        Args:
            
        Returns:
            List[int]: All values that the hand can be, in increasing order

        """
        BUST_VALUE = 21
        max_sum = 0
        number_aces = 0
        
        for card in self.cards:
            if(card.rank == Rank.ACE):
                number_aces += 1
                max_sum += card.rank_value[1]
            else:
                max_sum += card.rank_value[0]
        possible_values = []
        if(number_aces):
            if(max_sum <= BUST_VALUE):
                possible_values.append(max_sum)
            while number_aces > 0 and max_sum > 0:
                max_sum -= 10
                number_aces -= 1
                if(max_sum <= BUST_VALUE):
                    possible_values.append(max_sum)
            possible_values.reverse()
            return possible_values
        else:
            return [max_sum] if max_sum <= BUST_VALUE else []

