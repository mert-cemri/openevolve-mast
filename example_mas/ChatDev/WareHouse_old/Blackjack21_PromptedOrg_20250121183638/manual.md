# Blackjack Game User Manual

Welcome to the Blackjack Game! This manual will guide you through the installation, setup, and gameplay of our Blackjack card game application.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Gameplay Instructions](#gameplay-instructions)
4. [Main Features](#main-features)
5. [Troubleshooting](#troubleshooting)
6. [Contact Support](#contact-support)

## Introduction

The Blackjack Game is a Python-based application that simulates the classic card game of Blackjack, also known as 21. The game follows standard Blackjack rules, where the dealer hits up to 16 and stands on 17 or above. Players can choose to 'hit', 'stand', or 'double down' when appropriate. The game tracks totals, detects busts, and determines the winner after each round.

## Installation

To run the Blackjack Game, you need to have Python installed on your system. Follow these steps to set up the environment and install necessary dependencies:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Download the game files from the repository or copy the provided code into your local directory.

3. **Install Dependencies**: This game does not require any external Python packages beyond the standard library. However, if you plan to modify or extend the game, ensure you have a Python environment set up using `venv` or `conda`.

4. **Run the Game**: Navigate to the directory containing the game files and execute the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

## Gameplay Instructions

1. **Starting the Game**: Run the `main.py` file to start the game. You will be greeted with a welcome message.

2. **Placing Bets**: You will be prompted to place your bet. Enter a valid amount within your balance to proceed.

3. **Initial Deal**: Both the player and the dealer receive two cards. The dealer's second card remains hidden initially.

4. **Player Actions**: Choose from the following actions:
   - **Hit**: Draw another card.
   - **Stand**: Keep your current hand and end your turn.
   - **Double Down**: Double your bet, draw one more card, and end your turn.

5. **Dealer's Turn**: The dealer reveals their hidden card and plays according to the rules (hits until reaching 17 or higher).

6. **Determine Winner**: The game compares the player's and dealer's hands to determine the winner. The player wins if their hand value is higher than the dealer's without exceeding 21.

## Main Features

- **Card Deck Management**: The game uses a standard deck of 52 cards, shuffled at the start of each game.
- **Player and Dealer Logic**: Implements standard Blackjack rules for both player actions and dealer behavior.
- **Betting System**: Allows players to place bets and manage their balance.
- **Game Flow Management**: Handles the sequence of actions from dealing cards to determining the winner.

## Troubleshooting

- **Insufficient Balance**: If you try to place a bet higher than your balance, the game will prompt you to enter a valid amount.
- **Invalid Input**: Ensure you enter valid commands when prompted for actions (e.g., 'hit', 'stand', 'double down').

## Contact Support

If you encounter any issues or have questions about the game, please contact our support team at support@chatdev.com. We are here to help!

Enjoy playing Blackjack and good luck!