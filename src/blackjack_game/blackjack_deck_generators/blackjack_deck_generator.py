from typing import List, Protocol
from blackjack_game.card import Card
from blackjack_game.deck_generators.deck_generator import Deck_Generator 

class BlackJack_Deck_Generator(Protocol):
    """
    Builds a blackjack shoe/deck using a deck_generator

    Args:
        generator (DeckGenerator): Builds a single deck
        num_decks (int): The number of decks that makes up a shoe
    Returns:
        List[Card]: The blackjack shoe/deck that was created  
    
    """
    def generate_blackjack_deck(self, generator: Deck_Generator, num_decks: int) -> List[Card]:
        pass