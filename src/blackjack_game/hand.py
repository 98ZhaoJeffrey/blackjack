from blackjack_game.actions import default_split_rule
from blackjack_game.card import Card, Rank
from typing import List, Dict, Optional, Protocol
from dataclasses import dataclass
from blackjack_game.exceptions.HandSplitException import HandSplitException

@dataclass
class Hand():
    cards: List[Card]
    is_standing: bool = False
    is_doubled: bool = False
    is_busted: bool = False

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def split(self) -> Card:
        """
        Splits the hand

        Args:

        Returns:
            Card: The card that is split into the new hand
        """
        can_split_cards = default_split_rule(self) 
        if(can_split_cards):
            return self.cards.pop()
        else:
            raise HandSplitException(f"Can't split {self.cards[0]} and {self.cards[1]}")
    
    def get_valid_hand_values(self) -> List[int]:
        """
        Generates all possible hand values without busting

        Args:
            
        Returns:
            List[int]: All values that the hand can be, in increasing order

        """
        max_sum = 0
        number_aces = 0
        possible_values = []
        for card in self.cards:
            if(card.rank == Rank.ACE):
                number_aces += 1
                max_sum += card.rank_value[1]
            else:
                max_sum += card.rank_value[0]

        while number_aces > 0 and max_sum > 0:
            max_sum -= 10
            number_aces -= 1
            if(max_sum <= 21):
                possible_values.append(max_sum)
        possible_values.reverse()
        return possible_values

