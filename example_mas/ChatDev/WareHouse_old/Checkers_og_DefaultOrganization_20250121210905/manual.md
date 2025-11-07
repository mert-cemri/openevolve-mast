# Checkers Game User Manual

Welcome to the Checkers Game application! This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to play the game.

## Overview

The Checkers Game is a digital version of the classic board game, designed for two players. It features an 8x8 board, alternating turns between players, and includes standard capture and kinging rules. The game is implemented in Python using the Pygame library for graphical rendering.

## Installation

### Prerequisites

Before you can run the Checkers Game, ensure that you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Installing Dependencies

The game requires the Pygame library. You can install it using pip:

```bash
pip install pygame==2.1.2
```

Alternatively, you can install the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Running the Game

To start the game, navigate to the directory containing the game files and run the `main.py` script:

```bash
python main.py
```

This will launch the Checkers Game window, where you can begin playing.

## How to Play

### Game Setup

- The game board consists of 8 rows and 8 columns, with alternating dark and light squares.
- Each player starts with 12 pieces, placed on the dark squares of the first three rows closest to them.
- The two players are distinguished by color: Red and Black.

### Game Rules

- Players take turns moving their pieces diagonally forward on the dark squares.
- A piece can capture an opponent's piece by jumping over it to an empty square directly beyond.
- If a piece reaches the opposite end of the board, it is crowned as a "king" and can move both forward and backward.

### Making a Move

- Click on a piece to select it. The piece must belong to the current player.
- Click on a valid destination square to move the selected piece.
- If a capture is possible, the piece will jump over the opponent's piece and remove it from the board.
- The game alternates turns between the Red and Black players.

### Winning the Game

- The game ends when one player captures all of the opponent's pieces or blocks them from making any legal moves.

## Troubleshooting

If you encounter any issues while running the game, ensure that:

- Python and Pygame are correctly installed.
- You are using the correct version of Pygame as specified in the `requirements.txt`.
- Your system meets the necessary requirements to run Pygame applications.

For further assistance, feel free to reach out to our support team.

Enjoy playing the Checkers Game!