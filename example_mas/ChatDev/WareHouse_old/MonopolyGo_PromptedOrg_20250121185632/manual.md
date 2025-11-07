# Monopoly Go! Simplified Version

Welcome to the simplified version of Monopoly Go! This application simulates a basic version of the classic board game, Monopoly, with essential mechanics such as rolling dice, moving around properties, buying them, collecting rent, and handling chance events. The game tracks player money and property ownership, displaying relevant game information and prompting each player for decisions.

## Main Functions

- **Rolling Dice**: Players roll two six-sided dice to determine their movement on the board.
- **Moving Around Properties**: Players move around the board based on the dice roll.
- **Buying Properties**: Players can buy properties they land on if they are unowned and the player has enough money.
- **Collecting Rent**: Players pay rent when they land on properties owned by other players.
- **Handling Chance Events**: Players draw chance cards that can have various effects on their game status.
- **Tracking Player Money and Property Ownership**: The game keeps track of each player's money and the properties they own.
- **Game Information Display**: The game displays relevant information and prompts players for decisions.

## Installation

To run the game, you need to have Python installed on your system. Follow the steps below to set up the environment and run the game:

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation Steps

1. **Clone the Repository**: Clone the repository containing the game code to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: The game does not have any external dependencies beyond Python itself. Ensure Python is installed on your system.

3. **Run the Game**: Execute the main script to start the game.

   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script to start the game. The game will initialize with two players by default.

2. **Game Flow**: The game proceeds in turns. Each player rolls the dice and moves around the board. Depending on the space they land on, they can buy properties, pay rent, or draw chance cards.

3. **Buying Properties**: If a player lands on an unowned property and has enough money, they automatically buy it.

4. **Paying Rent**: If a player lands on a property owned by another player, they pay rent to the owner.

5. **Chance Cards**: Landing on a chance space allows the player to draw a chance card, which can have positive or negative effects.

6. **Winning the Game**: The game continues until only one player remains with money. The last player standing is declared the winner.

## Additional Information

- **Player Bankruptcy**: If a player's money drops to zero or below, they are declared bankrupt and removed from the game.
- **Game Customization**: You can customize the game by modifying the board layout, property prices, rents, and chance card effects in the respective Python files.

Enjoy playing the simplified version of Monopoly Go! and experience the classic board game in a digital format.