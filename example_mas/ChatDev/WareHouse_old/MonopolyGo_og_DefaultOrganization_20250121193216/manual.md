```markdown
# Monopoly Go! Simplified Version

Welcome to the simplified version of Monopoly Go! This application simulates a basic version of the classic board game, allowing players to roll dice, move around the board, buy properties, pay rent, and experience chance events. The game tracks player money and property ownership, displaying relevant game information and prompting each player for decisions.

## Main Functions

- **Rolling Dice**: Players roll a virtual dice to determine their movement on the board.
- **Moving Around Properties**: Players move around the board based on the dice roll.
- **Buying Properties**: Players can purchase properties they land on if they are not already owned.
- **Collecting Rent**: Players collect rent from opponents who land on their properties.
- **Handling Chance Events**: Chance events are integrated into the game to add unpredictability.
- **Tracking Player Money and Property Ownership**: The game keeps track of each player's money and properties owned.
- **Displaying Game Information**: The game displays current player information and prompts for decisions.

## Installation

### Environment Setup

This application is written in Python and requires Python to be installed on your system. No external dependencies are required for this implementation.

1. **Install Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the game code to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your directory to the project folder.

   ```bash
   cd <project-directory>
   ```

4. **Run the Game**: Execute the main script to start the game.

   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script to initialize the game.

2. **Game Interface**: The game can run in both GUI and non-GUI modes. If a graphical interface is available, it will display the game board and player information. Otherwise, the game will run in the console.

3. **Player Turns**: Each player takes turns rolling the dice. The game will display whose turn it is and their current money.

4. **Buying Properties**: When a player lands on an unowned property, they will be prompted to buy it. The player can choose to purchase the property if they have enough money.

5. **Paying Rent**: If a player lands on a property owned by another player, they must pay rent to the owner.

6. **Winning the Game**: The game continues until only one player remains with money. The player with the most money at the end is declared the winner.

7. **Exiting the Game**: The game will automatically end when a winner is determined. You can also close the game window or stop the console execution to exit.

Enjoy playing Monopoly Go! and may the best strategist win!
```