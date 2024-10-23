from cards import Card, Minion, Spell  # Import card classes for use in the hand

class Hand:
    def __init__(self):
        self.cards = []  # Initialize an empty list to store cards in hand

    def add_card(self, card):
        # Add a card to the hand
        self.cards.append(card)

    def play_card(self, card_index, player, target=None):
        # Play a card from the hand based on the index
        if 0 <= card_index < len(self.cards):
            card = self.cards.pop(card_index)  # Remove the card from hand
            card.play(player, target)  # Play the card using the play method
            return card  # Return the played card
        else:
            return None  # Return None if the index is invalid

    def display_hand(self):
        # Display the current cards in the hand
        if self.cards:
            print("Current hand:")
            for index, card in enumerate(self.cards):
                # Print each card's index, name, mana cost, and description
                print(f"{index}: {card.name} (Cost: {card.mana_cost}) - {card.description}")
        else:
            print("Hand is empty.")  # Indicate that the hand has no cards
