# Dou Dizhu Game User Manual

Welcome to the Dou Dizhu game, a digital implementation of the popular Chinese card game for three players. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to play the game.

## Table of Contents

1. [Introduction](#introduction)
2. [Quick Install](#quick-install)
3. [Main Functions](#main-functions)
4. [How to Play](#how-to-play)
5. [Game Rules](#game-rules)

## Introduction

Dou Dizhu is a strategic card game involving three players, one of whom is designated as the 'landlord.' The objective is to be the first to run out of cards or to prevent the landlord from doing so. This software provides a digital platform to enjoy Dou Dizhu with automated card dealing and game management.

## Quick Install

To install and run the Dou Dizhu game, ensure you have Python installed on your system. This game does not require any external dependencies, so installation is straightforward.

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game:**
   ```bash
   python main.py
   ```

## Main Functions

The Dou Dizhu game software includes several key components:

- **Deck Management:** Handles the creation and shuffling of the card deck.
- **Player Management:** Manages player information and actions.
- **Game Flow:** Controls the overall game process, including dealing cards, determining the landlord, and managing turns.
- **Hand Evaluation:** Validates the combinations of cards played by the players.

## How to Play

1. **Start the Game:**
   - Run the `main.py` script to initialize the game.
   - The game will automatically shuffle the deck and deal cards to the three players.

2. **Determine the Landlord:**
   - The game will select the first player as the landlord by default and assign the extra landlord cards to them.

3. **Playing the Game:**
   - Players take turns playing valid combinations of cards.
   - The game will prompt each player in turn to play their hand.
   - The player can play a single card or a valid combination as per the rules.

4. **Winning the Game:**
   - The first player to run out of cards wins the game.
   - If the landlord runs out of cards first, they win.

## Game Rules

- **Valid Combinations:** Players can play singles, pairs, triples, straights, and other valid combinations.
- **Landlord Advantage:** The landlord receives extra cards and plays first.
- **Objective:** Be the first to play all your cards or prevent the landlord from doing so.

Enjoy playing Dou Dizhu and may the best strategist win! If you encounter any issues or have questions, please refer to the documentation or contact support.