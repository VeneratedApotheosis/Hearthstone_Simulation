# deck.py
import random
from cards import Card  # Import the Card class for card-related functionalities

class Deck:
    def __init__(self, cards):
        self.cards = cards  # Initialize the deck with a list of cards

    def shuffle(self):
        # Shuffle the cards in the deck randomly
        random.shuffle(self.cards)

    def draw_card(self):
        # Draw the top card from the deck
        if self.cards:
            card = self.cards.pop(0)  # Remove and return the top card
            return card
        return None  # Return None if the deck is empty
