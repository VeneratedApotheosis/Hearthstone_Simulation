from cards import Card, Minion, Spell
from deck import Deck
from player import Player
from utils import *
from game import minions, spells, game_loop

# Create decks for each player and initialize with minions and spells
deck1 = Deck(minions + spells)
deck2 = Deck(minions + spells)

# Shuffle the decks to randomize the card order
deck1.shuffle()
deck2.shuffle()

# Create player instances with their respective decks
player1 = Player("Player 1", deck1)
player2 = Player("Player 2", deck2)

# Each player draws a starting hand of cards
player1.draw_starting_hand()
player2.draw_starting_hand()

# Start the main game loop to begin gameplay
game_loop(player1, player2)
