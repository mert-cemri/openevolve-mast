# Blackjack Game User Manual

Welcome to the Blackjack Game! This manual will guide you through the installation, setup, and usage of the Blackjack card game application. This game follows the standard rules of Blackjack, where the dealer hits up to 16 and stands on 17 or above. The player can choose to 'hit,' 'stand,' or 'double down' when appropriate. The game tracks totals, detects busts, and determines the winner after each round.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Game Setup](#game-setup)
4. [How to Play](#how-to-play)
5. [Game Rules](#game-rules)
6. [Contact and Support](#contact-and-support)

## Introduction

The Blackjack Game is a Python-based application that simulates the classic card game of Blackjack. It is designed to provide an interactive and engaging experience for players who enjoy card games. The game is played against a dealer, and the objective is to have a hand value closer to 21 than the dealer's hand without exceeding 21.

## Installation

To run the Blackjack Game, you need to have Python installed on your system. Follow these steps to set up the game environment:

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the game repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Game Directory**: Change your directory to the game folder:
   ```bash
   cd <repository-folder>
   ```

4. **Install Dependencies**: Install any required dependencies using pip. If there are any specific dependencies, they will be listed in a `requirements.txt` file. Use the following command to install them:
   ```bash
   pip install -r requirements.txt
   ```

## Game Setup

Once you have installed the necessary dependencies, you can start the game by running the main module. Use the following command to launch the game:

```bash
python main.py
```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. The game will shuffle the deck and deal two cards each to the player and the dealer.

2. **Player Actions**: You will be prompted to choose an action:
   - **Hit**: Draw another card to increase your hand value.
   - **Stand**: Keep your current hand and end your turn.
   - **Double Down**: Double your bet, draw one more card, and end your turn.

3. **Dealer's Turn**: After the player's turn, the dealer will reveal their hidden card and draw cards until their hand value is at least 17.

4. **Determine the Winner**: The game will compare the player's and dealer's hand values to determine the winner. The winner is announced based on the standard Blackjack rules.

## Game Rules

- The goal is to have a hand value closer to 21 than the dealer without exceeding 21.
- Number cards are worth their face value, face cards (J, Q, K) are worth 10, and Aces can be worth 1 or 11.
- The dealer must hit until their hand value is 17 or higher.
- If the player or dealer exceeds 21, they bust and lose the round.
- In case of a tie, the round is a draw.

## Contact and Support

For any questions, issues, or support, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com). We are here to assist you with any inquiries or technical difficulties you may encounter.

Enjoy playing the Blackjack Game and may the best hand win!