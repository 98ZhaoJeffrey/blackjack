from typing import List, Protocol
from blackjack_game.card import Card

class Deck_Generator(Protocol):
    """
    Builds a list of cards that is our "deck"

    Args:

    Returns:
        List[Card]: The "deck" that was created  
    
    """
    def generate_deck(self) -> List[Card]:
        pass