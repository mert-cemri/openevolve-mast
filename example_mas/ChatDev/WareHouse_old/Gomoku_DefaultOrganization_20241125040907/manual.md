# Gomoku Game User Manual

Welcome to the Gomoku game! This user manual will guide you through the installation process and explain how to use and play the game.

## Table of Contents
1. [Installation](#installation)
2. [Game Overview](#game-overview)
3. [Playing the Game](#playing-the-game)
4. [Winning the Game](#winning-the-game)

## 1. Installation <a name="installation"></a>

To install and run the Gomoku game, please follow these steps:

1. Make sure you have Python installed on your computer. If not, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the game files from the provided source.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the game files.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary dependencies, including tkinter.

5. Once the installation is complete, you can start the game by running the following command:

   ```
   python main.py
   ```

   The game window should open, and you are ready to play!

## 2. Game Overview <a name="game-overview"></a>

Gomoku is a two-player strategy board game. The goal of the game is to be the first player to form a horizontal, vertical, or diagonal line of five stones of your color on the game board.

The game board consists of a 15x15 grid, where players take turns placing their stones on empty intersections. The first player uses black stones, and the second player uses white stones.

## 3. Playing the Game <a name="playing-the-game"></a>

To make a move in the game, follow these steps:

1. Click on an empty intersection on the game board. The intersection will be highlighted with your stone color.

2. The game will automatically switch to the other player's turn.

3. Repeat the process, taking turns with the other player, until one player wins or the game ends in a draw.

## 4. Winning the Game <a name="winning-the-game"></a>

The game ends when one player successfully forms a line of five stones of their color, either horizontally, vertically, or diagonally. When this happens, the game will display a message indicating the winner.

If the game board is filled with stones and no player has formed a line of five, the game ends in a draw.

Enjoy playing Gomoku and have fun!