from player import Player
from cards import Card, Minion, Spell
from deck import Deck
from player import Player
from utils import *

def game_loop(player1, player2):
    players = [player1, player2]  # List of players in the game
    current_player = 0  # Index to track the current player

    while True:
        opponent = players[(current_player + 1) % 2]  # Get the opponent player
        print(f"\n===== {players[current_player].name}'s Turn =====")

        # Execute the current player's turn and check for game over
        game_over = players[current_player].take_turn(opponent)
        if game_over:
            print(f"\n{players[current_player].name} wins!")  # Announce the winner
            break

        # Switch to the other player for the next turn
        current_player = (current_player + 1) % 2

