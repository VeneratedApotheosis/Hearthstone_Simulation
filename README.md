# Hearthstone_Simulation
Project Structure

The project is organized into several modules, each with specific responsibilities:
1. cards.py

Defines the basic structure of cards in the game.

    Classes:
        Card: Base class for all cards with common attributes and methods.
        Minion: Represents minion cards with attack and health values, along with methods for playing and attacking.
        Spell: Represents spell cards that can affect minions or players, with specific effects.

2. deck.py

Handles the creation and management of decks.

    Classes:
        Deck: Manages a collection of cards, allowing shuffling and drawing of cards.
        Hand: Manages the player's hand of cards, including adding, playing, and displaying cards.

3. board.py

Manages the battlefield where minions are played.

    Classes:
        Battlefield: Tracks the minions currently on the battlefield, providing methods to add or remove minions and display their status.

4. player.py

Represents each player in the game.

    Classes:
        Player: Manages a player's deck, hand, battlefield, mana crystals, and health. It handles drawing cards and taking turns.

5. utils.py

Contains utility functions for various spell effects and game mechanics.

    Functions include spell effects like fireball_effect, polymorph_effect, flamestrike_effect, and others that modify game states.

6. main.py

The entry point of the game, setting up players and starting the game loop.

    Initializes decks, draws starting hands, and starts the game loop.

7. game.py

Handles the main game loop, managing turns between players and checking for win conditions.

    Function:
        game_loop: Manages player turns and checks for the end of the game.

How to Run

To play the game, simply execute the main.py file. Ensure that all modules are in the same directory. Follow the on-screen prompts to play the game.
