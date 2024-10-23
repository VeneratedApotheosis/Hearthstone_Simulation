from cards import Minion, Spell, Card  # Import card classes for use on the battlefield

class Battlefield:
    def __init__(self):
        self.minions = []  # Initialize an empty list to store minions on the battlefield

    def add_minion(self, minion):
        # Add a minion to the battlefield if there's space
        if len(self.minions) < 7:
            self.minions.append(minion)
        else:
            print("Battlefield is full. Cannot add more minions.")  # Indicate if the battlefield is full

    def remove_minion(self, minion):
        # Remove a minion from the battlefield if it exists
        if minion in self.minions:
            print(f"{minion.name} is dead")  # Inform that the minion has died
            self.minions.remove(minion)  # Remove the minion from the list
        else:
            print("Minion not found on the battlefield.")  # Indicate if the minion is not present

    def display_battlefield(self):
        # Display the current state of minions on the battlefield
        print("Current Minions on the Battlefield:")
        for index, minion in enumerate(self.minions):
            # Print each minion's index, name, attack, and health
            print(f"{index}: {minion.name} - {minion.attack}/{minion.health} HP")
