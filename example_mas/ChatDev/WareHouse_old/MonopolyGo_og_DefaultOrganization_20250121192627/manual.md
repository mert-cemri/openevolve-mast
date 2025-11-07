# Monopoly Go! User Manual

Welcome to Monopoly Go!, a simplified version of the classic board game. This application allows you to enjoy the essential mechanics of Monopoly, including rolling dice, moving around the board, buying properties, collecting rent, and handling chance events. This manual will guide you through the installation process, introduce the main functions of the software, and explain how to play the game.

## Quick Install

Monopoly Go! is developed in Python and does not require any external dependencies. However, you need to have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Clone the repository using the following command:
     ```bash
     git clone <repository-url>
     ```
   - Navigate to the cloned directory:
     ```bash
     cd <repository-directory>
     ```

2. **Run the Game:**
   - Execute the main script to start the game:
     ```bash
     python main.py
     ```

## Main Functions of the Software

Monopoly Go! includes several key features that replicate the classic board game experience:

- **Rolling Dice:** Players roll two six-sided dice to determine their movement around the board.
- **Property Management:** Players can buy properties, collect rent from opponents, and manage their property portfolio.
- **Chance Events:** Players draw chance cards that can have various effects, such as gaining or losing money, moving to different board positions, or receiving special benefits.
- **Player Management:** The game tracks player money, property ownership, and other relevant statistics.

## How to Play

1. **Starting the Game:**
   - Launch the game by running `python main.py`.
   - The game will open a graphical user interface (GUI) where you can see the current game state.

2. **Taking Turns:**
   - The game alternates turns between players.
   - On your turn, click the "Roll Dice" button to roll the dice and move your token around the board.
   - The game will automatically handle property purchases, rent payments, and chance events based on your new position.

3. **Managing Properties:**
   - If you land on an unowned property and have enough money, you can choose to buy it.
   - If you land on a property owned by another player, you will pay rent to the owner.

4. **Handling Chance Events:**
   - When you land on a chance space, a chance card will be drawn, and its effects will be applied automatically.

5. **Winning the Game:**
   - The game continues until a player goes bankrupt or you decide to end the game manually.

## Additional Information

- **Headless Mode:** If you are running the game in an environment without a display (e.g., a server), the game will automatically switch to a non-GUI mode and print game information to the console.
- **Game Customization:** You can modify the properties and chance cards by editing the `board.py` file to customize your game experience.

Enjoy playing Monopoly Go! and may the best strategist win!