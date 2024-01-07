from typing import List, Protocol
from blackjack_game.card import Card
from blackjack_game.deck_generators.deck_generator import Deck_Generator 
from blackjack_game.blackjack_deck_generators.blackjack_deck_generator import BlackJack_Deck_Generator

class Default_BlackJack_Deck_Generator(BlackJack_Deck_Generator):
    """
    Builds a blackjack shoe/deck using a deck_generator

    Args:
        generator (DeckGenerator): Builds a single deck
        num_decks (int): The number of decks that makes up a shoe
    Returns:
        List[Card]: The blackjack shoe/deck that was created  
    
    """
    def generate_blackjack_deck(self, generator: Deck_Generator, num_decks: int) -> List[Card]:
        decks = [generator.generate_deck() for _ in range(num_decks)]
        new_deck = []
        for deck in decks:
            new_deck += deck
        return new_deck