from typing import List
from blackjack_game.deck_generators.deck_generator import Deck_Generator
from blackjack_game.card import Card, Rank, Suit

class Default_Deck_Generator(Deck_Generator):
    """
    Builds a list of cards that is our "deck"

    Args:

    Returns:
        List[Card]: The "deck" that was created  
    
    """
    def generate_deck(self) -> List[Card]:
        deck = []
        for rank in Rank:
            for suit in Suit:
                deck.append(Card(rank, suit))
        return deck