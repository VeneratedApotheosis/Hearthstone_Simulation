# utils.py
from cards import *
from player import *
from deck import *
from board import *
from hand import *


#Effects that all spells will have when played during games
def fireball_effect(player,enemy,target):
    target.health -= 6
    print(f"Dealt 6 damage to {target.name}")

def polymorph_effect(target):
    target.attack = 1
    target.health = 1
    target.name = "Sheep"

def flamestrike_effect(player,enemy,targets):
    enemy_minions = enemy.battlefield.minions
    for minion in enemy_minions:
        minion.health -= 5
        print(f"Dealt 5 damage to {minion.name}, it has {minion.health} health remaining.")

def arcane_intellect_effect(player,enemy,target):
    player.draw_card()
    player.draw_card()
    print(f"{player.name} draws 2 cards.")

def polymorph_effect(player,enemy,target):
    target.attack = 1
    target.health = 1
    target.name = "Sheep"
    print(f"Transformed {target.name} into a 1/1 Sheep.")

def cataclysm_effect(player,enemy,target):
    battlefield = player.battlefield.minions
    battlefieldEnemy = enemy.battlefield.minions
    for minion in battlefield:
        player.battlefield.remove_minion(minion)
    for minion in battlefieldEnemy:
        player.battlefield.remove_minion(minion)
    player.discard(2)
    print(f"{player.name} discards 2 cards.")

import random
def deadly_shot_effect(player,enemy,target):
    enemy_minions = enemy.battlefield.minions
    if enemy_minions:
        target = random.choice(enemy_minions)
        print(f"Deadly Shot destroys {target.name}.")
        enemy_minions.remove(target)

def holy_nova_effect(player,enemy,target):
    enemy_minions = enemy.battlefield.minions
    for minion in enemy_minions:
        minion.health -= 2
        print(f"Dealt 2 damage to {minion.name}, it has {minion.health} health remaining.")
    for minion in player.battlefield.minions:
        minion.health += 2
        print(f"Restored 2 health to {minion.name}, it now has {minion.health} health.")
    player.health += 2
    print(f"Restored 2 health to {player.name}, it now has {player.health} health.")

#Minion list : lists out all minions that are in the game, used for decks
stormwind_champion = Minion(
    name="Stormwind Champion",
    mana_cost=7,
    attack=6,
    health=6,
    description="Your other minions have +1/+1.",
    effects=["+1/+1 to other minions"]
)
booty_bay_bodyguard = Minion(
    name="Booty Bay Bodyguard",
    mana_cost=5,
    attack=5,
    health=4,
    description="Taunt",
    effects=["Taunt"]
)
wolfrider = Minion(
    name="Wolfrider",
    mana_cost=3,
    attack=3,
    health=1,
    description="Charge",
    effects=["Charge"]
)
spymistress = Minion(
    name="Spymistress",
    mana_cost=1,
    attack=3,
    health=1,
    description="Stealth",
    effects=["Stealth"]
)
chilliwindyeti = Minion(
    "Chillwind Yeti", 
    4, 
    4, 
    5, 
    "Yeti."
    )
boulderfistogre = Minion(
    "Boulderfist Ogre", 
    6, 
    6, 
    7, 
    "Ogre."
)
bloodfenraptor = Minion(
    "Bloodfen Raptor", 
    2, 
    3, 
    2, 
    "Raptor."
)

minions = [
    stormwind_champion,
    booty_bay_bodyguard,
    wolfrider,
    spymistress,
    chilliwindyeti,
    boulderfistogre,
    bloodfenraptor
]

# Spell list : lists out all spells that are in the game, used for decks
spells = [
    Spell(
        name="Flamestrike",
        mana_cost=7,
        description="Deal 5 damage to all enemy minions.",
        effect=flamestrike_effect
    ),
    Spell(
        name="Arcane Intellect",
        mana_cost=3,
        description="Draw 2 cards.",
        effect=arcane_intellect_effect
    ),
    Spell(
        name="Polymorph",
        mana_cost=4,
        description="Transform a minion into a 1/1 Sheep.",
        effect=polymorph_effect
    ),
    Spell(
        name="Cataclysm",
        mana_cost=5,
        description="Destroy all minions. Discard 2 cards.",
        effect=cataclysm_effect
    ),
    Spell(
        name="Deadly Shot",
        mana_cost=3,
        description="Destroy a random enemy minion.",
        effect=deadly_shot_effect
    ),
    Spell(
        name="Holy Nova",
        mana_cost=3,
        description="Deal 2 damage to all enemy minions. Restore 2 Health to all friendly characters.",
        effect=holy_nova_effect
    )
]
