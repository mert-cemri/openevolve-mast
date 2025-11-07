# Dou Dizhu Game User Manual

Welcome to the Dou Dizhu Game, a digital implementation of the popular Chinese poker game designed for three players. This manual will guide you through the main functions of the software, installation of environment dependencies, and instructions on how to play the game.

## Main Functions

The Dou Dizhu Game application provides the following main functions:

- **Game Setup**: Automatically shuffles and deals cards to three players, designating one as the 'landlord'.
- **Turn-Based Play**: Players take turns to play valid card combinations, aiming to be the first to run out of cards or prevent the landlord from doing so.
- **Card Combinations**: Supports various card combinations such as singles, pairs, and more complex sequences.
- **Graphical User Interface (GUI)**: A simple GUI to facilitate gameplay, display player hands, and manage turns.
- **Winner Announcement**: Automatically detects and announces the winner when a player runs out of cards.

## Installation

### Prerequisites

Ensure you have Python installed on your system. The game uses the Python standard library, so no additional external dependencies are required.

### Quick Install

1. **Clone the Repository**: Download the source code from the repository.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game**: Execute the main script to start the game.

   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Launch the game by running the `main.py` script. The GUI will open, displaying the initial game state.

2. **Game Interface**: The GUI shows each player's hand and indicates whose turn it is.

3. **Playing a Turn**:
   - Select the cards you wish to play (this feature is currently a placeholder and requires manual input in the code).
   - Click the "Play Turn" button to submit your selected cards.
   - The game will validate your move and update the display accordingly.

4. **Winning the Game**: The first player to run out of cards wins the game. The game will automatically announce the winner and end the session.

5. **Game Rules**: Follow standard Dou Dizhu rules for valid card combinations and turn progression. The game logic checks for valid moves and ensures fair play.

## Documentation

For further details on the game logic and code structure, please refer to the source code files included in the repository. Each file contains comments explaining the functionality of classes and methods.

We hope you enjoy playing Dou Dizhu! If you encounter any issues or have suggestions for improvements, please contact our support team.