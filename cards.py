# cards.py
class Card:
    def __init__(self, name, mana_cost, description):
        self.name = name  # Name of the card
        self.mana_cost = mana_cost  # Mana cost to play the card
        self.description = description  # Description of the card's effect
    
    def play(self, player, target=None):
        pass  # To be overridden by derived classes

class Minion(Card):
    def __init__(self, name, mana_cost, attack, health, description, effects=None):
        super().__init__(name, mana_cost, description)
        self.attack = attack  # Attack value of the minion
        self.health = health  # Health value of the minion
        self.effects = effects or []  # List of effects the minion may have

    def play(self, player, target=None):
        # Summon the minion and add it to the battlefield
        print(f"{self.name} has been summoned with {self.attack} attack and {self.health} health.")
        player.battlefield.add_minion(self)

    def attack_minion(self, target):
        target.health -= self.attack  # Deduct target's health
        self.health -= target.attack  # Deduct minion's health from counterattack
        print(f"{self.name} attacks {target.name}, dealing {self.attack} damage!")
        
        if self.health <= 0:
            print(f"{self.name} has died.")  # Minion dies if health is 0 or less
            return True
        if target.health <= 0:
            print(f"{target.name} has died.")  # Target dies if health is 0 or less
            return False
        return None  # No death occurred

class Spell(Card):
    def __init__(self, name, mana_cost, description, effect):
        super().__init__(name, mana_cost, description)
        self.effect = effect  # The effect function that the spell will invoke

    def play(self, player, enemy, target):
        # Execute the spell's effect on the target
        print(f"Playing spell {self.name}.")
        self.effect(target)
