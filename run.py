from blackjack_game.deck import Deck
from src.blackjack_game.game import Game
from src.blackjack_game.players import RandomPlayer, TerminalPlayer

def main():
    game = Game(Deck(number_decks=8))
    game.add_player(TerminalPlayer(name="TerminalPlayer", bankroll=1000, bet=100))
    game.add_player(RandomPlayer(name="RandomPlayer", bankroll=1000, bet=100))
    game.play_hand()

if __name__ == "__main__":
    main()