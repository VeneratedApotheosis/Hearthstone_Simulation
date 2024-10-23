from board import Battlefield
from hand import Hand
from deck import Deck
from cards import Card, Minion, Spell

class Player:
    def __init__(self, name, deck):
        self.name = name  # Player's name
        self.deck = deck  # Player's deck of cards
        self.hand = Hand()  # Player's hand containing cards
        self.battlefield = Battlefield()  # Player's battlefield for minions
        self.mana_crystals = 0  # Player's available mana crystals
        self.health = 30  # Player's health points

    def draw_starting_hand(self):
        # Draw three cards to start the game
        for _ in range(3):
            card = self.deck.draw_card()
            if card:
                self.hand.add_card(card)

    def take_turn(self, opponent):
        # Start player's turn, increase mana and draw a card
        self.mana_crystals += 1
        card = self.deck.draw_card()
        if card:
            self.hand.add_card(card)

        # Display current status
        print(f"Mana Crystals: {self.mana_crystals}")
        print(f"{self.name}'s Health: {self.health}")
        self.hand.display_hand()
        
        print("\nYour field")
        self.battlefield.display_battlefield()
        
        print("\nOpponent field")
        opponent.battlefield.display_battlefield()

        # Loop for player's actions
        while True:
            print("\nActions:")
            print("1. Play a Card")
            print("2. Attack with a Minion")
            print("3. End Turn")

            action = input("Choose an action: ")

            if action == "1":  # Play a card action
                self.hand.display_hand()
                card_index = int(input("Select a card index to play: "))
                if 0 <= card_index < len(self.hand.cards):
                    card = self.hand.cards[card_index]
                    if self.mana_crystals >= card.mana_cost:
                        self.mana_crystals -= card.mana_cost
                        # Handling between playing a minion and a spell
                        if isinstance(card, Minion):
                            self.hand.play_card(card_index, self)  # Play the minion
                        else:
                            # Playing a spell
                            opponent.battlefield.display_battlefield()
                            target_index = int(input("Choose a target to use spell on: "))
                            if 0 <= target_index < len(opponent.battlefield.minions):
                                target = opponent.battlefield.minions[target_index]
                                card.play(self, opponent, target)  # Use the spell effect
                                if target.health <= 0:
                                    opponent.battlefield.remove_minion(target)  # Remove the minion if health drops to zero
                    else:
                        print("Not enough mana.")  # Error if not enough mana
            elif action == "2":  # Attack with a minion action
                if not self.battlefield.minions:
                    print("No minions to attack with.")  # Check if there are minions to attack
                    continue

                self.battlefield.display_battlefield()
                attacker_index = int(input("Choose an attacking minion index: "))
                if 0 <= attacker_index < len(self.battlefield.minions):
                    attacker = self.battlefield.minions[attacker_index]
                    if opponent.battlefield.minions:
                        opponent.battlefield.display_battlefield()
                        target_index = int(input("Choose a target minion to attack: ")) 
                        if 0 <= target_index < len(opponent.battlefield.minions):
                            target = opponent.battlefield.minions[target_index]
                            result = attacker.attack_minion(target)  # Execute the attack
                            if result:
                                self.battlefield.remove_minion(attacker)  # Remove attacker if it dies
                            if result is False:
                                opponent.battlefield.remove_minion(target)  # Remove target if it dies
                    else:
                        # If no enemy minions, attack the opponent directly
                        print("No enemy minions, attacking the player directly!")
                        opponent.health -= attacker.attack
                        print(f"{attacker.name} deals {attacker.attack} damage to {opponent.name}. {opponent.name}'s health is now {opponent.health}.")
                        if opponent.health <= 0:
                            print(f"{opponent.name} has been defeated!")  # Announce opponent's defeat
                            return True
            elif action == "3":  # End turn action
                print("Ending turn.")
                break
            else:
                print("Invalid action.")  # Error for invalid input
        return False
