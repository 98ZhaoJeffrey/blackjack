from enum import Enum
from typing import List, Dict, Optional, Any
from dataclasses import dataclass
from blackjack_game.actions import generate_valid_player_actions
from blackjack_game.player import Player
from blackjack_game.deck import Deck
from blackjack_game.hand import Hand
from blackjack_game.player import PlayerAction
from blackjack_game.observer.observer import Observer
from blackjack_game.observer.subject import Subject
from blackjack_game.blackjack_deck_generators.default_blackjack_deck_generator import Default_BlackJack_Deck_Generator
from blackjack_game.deck_generators.default_deck_generator import Default_Deck_Generator

@dataclass
class Game(Subject):

    players: List[Player]
    current_player: int
    dealers_hand: Hand
    deck: Deck
    observers: List[Observer]
    DEALER_STOPS_HIITING = 17

    def attach(self, observer: Observer) -> None:
        """
            Attach an observer to the subject.
        """
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify(self, data: Dict[str, Any], observer: Optional[Observer]) -> None:
        """
            Notify all observers about an event.
        """
        if(observer):
            observer.update(self, data)
        else:
            for obs in self.observers:
                obs.update(self, data)

    def add_player(self, player: Player) -> None:
        self.players.append(player)
    
    def remove_player(self, player: Player) -> None:
        self.players.remove(player)

    def _setup_hand(self) -> None:
        """
            Deal cards to players and dealer, making them face up as well

            Args:

            Returns:

        """
        for player in self.players:
            top_card = self.deck.deal()
            #top_card.flip_card()
            player.hands[0].cards.append(top_card)
        
        self.dealers_hand.cards.append(self.deck.deal())
        
        for player in self.players:
            top_card = self.deck.deal()
            #top_card.flip_card()
            player.hands[0].cards.append(top_card)
        
        self.dealers_hand.cards.append(self.deck.deal())
        #self.dealers_hand[0].flip_card()

    def _perform_dealer_action(self, actions: List[PlayerAction]) -> List[Hand]:
        """
            Perform the corresponding action based on the user's current action for the hand

            Args:
                actions (List[PlayerAction]): The actions that the player makes for each hand

            Returns:
                List[Hand]: The newly updated hands after performing the corresponding actions
        """
        # splitting hand requires us to insert in middle of list, not a good idea with for loop
        new_hands = []
        player = self.players[self.current_player]
        for action, hand in zip(actions, player.hands):
            new_hands.append(hand)
            if(action == PlayerAction.HIT):
                hand.add_card(self.deck.deal())
            elif(action == PlayerAction.STAND):
                hand.is_standing = True
            elif(action == PlayerAction.SPLIT):
                top_card = hand.split()
                split_hand = Hand(cards=[top_card])
                new_hands.append(split_hand)
            elif(action == PlayerAction.DOUBLE):
                hand.add_card(self.deck.deal())
                hand.is_doubled = True
        return new_hands
    
    def _play_dealers_hand(self) -> None:
        """
            Deal the cards for the dealer after action from all players has completed
            
            Args:

            Return:
        """
        #self.dealers_hand[1].flip_card()
        hand_values = self.dealers_hand.get_valid_hand_values()
        while(hand_values):
            largest_hand = max(hand_values)
            if(largest_hand >= self.DEALER_STOPS_HIITING):
                return
            else:
                next_card = self.deck.deal()
                #next_card.flip_card()
                self.dealers_hand.cards.append(next_card)
                hand_values = self.dealers_hand.get_valid_hand_values()
        self.dealers_hand.is_busted = True
        return

    
    def _create_payouts(self, hands: List[Hand]) -> List[int]:
        """
            Determine how much each hand should be paid out

            Args: 
                hand (List[Hand]): The hands that should be paid out
            
            Return:
                List[Int]: The multipler for each hand's payout
        """
        payouts = []

        all_dealers_value = self.dealers_hand.get_valid_hand_values()
        max_dealers_value = max(all_dealers_value) if all_dealers_value else 0

        for hand in hands:
            max_hand_value = max(hand.get_valid_hand_values())
            lost_game = hand.is_busted or max_hand_value  < max_dealers_value
            tied_game = max_hand_value == max_dealers_value
            won_game = max_hand_value >= max_dealers_value
            if(lost_game):
                payouts.append(-1)
            elif(tied_game):
                payouts.append(0)
            elif(won_game):
                payouts.append(1) 
        return payouts    


    def play_hand(self) -> None:

        """
        Plays a hand of blackjack

        Args:

        Return:

        """

        self._setup_hand()
        completed_hands = 0
        number_hands = sum(len(player.hands) for player in self.players)
        while completed_hands < number_hands:
            
            for player in self.players:
                for hand in player.hands:
                    if(not hand.get_valid_hand_values()):
                        hand.is_busted = True

            player_actions = []
            for player in self.players:
                curr_player_actions = []
                for hand in player.hands:
                    valid_actions = generate_valid_player_actions(hand)
                    if(not valid_actions):
                        completed_hands += 1
                        continue
                    curr_player_actions.append(player.make_action(valid_actions))
                player_actions.append(curr_player_actions)

            for player, actions in zip(self.players, player_actions):
                player.hands = self._perform_dealer_action(actions)
            
        self._play_dealers_hand()

        for player in self.players:
            payouts = self._create_payouts(player.hands)
            for payout in payouts:
                player.modify_bankroll(payout * player.bet)


    def setup_game(self) -> None:
        """
        Sets up the game of BlackJack
        """
        self.deck = Deck(number_decks=8, _blackjack_deck_builder=Default_BlackJack_Deck_Generator(), _deck_builder=Default_Deck_Generator())

