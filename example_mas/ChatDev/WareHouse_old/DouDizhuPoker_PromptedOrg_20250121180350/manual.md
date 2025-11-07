# Dou Dizhu Game User Manual

Welcome to the Dou Dizhu Game, a digital implementation of the popular Chinese card game for three players. This manual will guide you through the installation, setup, and gameplay of the Dou Dizhu application.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Game Setup](#game-setup)
4. [How to Play](#how-to-play)
5. [Game Rules](#game-rules)
6. [Troubleshooting](#troubleshooting)
7. [Contact and Support](#contact-and-support)

## Introduction

Dou Dizhu is a strategic card game played with a standard deck of cards, including two jokers. The game involves three players, one of whom is designated as the 'landlord.' The objective is to be the first to run out of cards or to prevent the landlord from doing so. This application simulates the Dou Dizhu game, allowing you to play against computer-controlled opponents.

## Installation

To run the Dou Dizhu game, you need to have Python installed on your system. Follow the steps below to set up the environment and install necessary dependencies.

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository:**

   Open your terminal or command prompt and run the following command to clone the repository:

   ```bash
   git clone https://github.com/yourusername/dou-dizhu.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd dou-dizhu
   ```

3. **Install Dependencies:**

   Use pip to install any required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Note: Ensure that the `requirements.txt` file is present in the project directory with all necessary dependencies listed.

## Game Setup

Once the installation is complete, you can start the game by running the main module. Execute the following command in your terminal:

```bash
python main.py
```

This will initialize the game and set up the players and deck.

## How to Play

1. **Starting the Game:**

   The game begins with the deck being shuffled and cards dealt to each player. One player is randomly chosen as the landlord.

2. **Playing Rounds:**

   Players take turns to play valid card combinations. The game will prompt each player to play their turn, displaying their current hand.

3. **Winning the Game:**

   The first player to run out of cards wins the game. If the landlord runs out of cards first, they win.

## Game Rules

- **Card Combinations:**
  - Singles: Any single card.
  - Pairs: Two cards of the same rank.
  - Straights: Five or more consecutive cards.
  - Additional combinations like triples, full houses, and bombs can be implemented.

- **Landlord Selection:**
  - The landlord is chosen randomly at the start of the game.

- **Objective:**
  - Be the first to play all your cards or prevent the landlord from doing so.

## Troubleshooting

- **Game Not Starting:**
  - Ensure Python is installed and the correct version is being used.
  - Check if all dependencies are installed correctly.

- **Invalid Card Combinations:**
  - Ensure you are playing valid combinations as per the rules.

## Contact and Support

For further assistance, please contact our support team at support@chatdev.com. We are here to help you with any issues or questions you may have.

Thank you for choosing our Dou Dizhu game. Enjoy playing!