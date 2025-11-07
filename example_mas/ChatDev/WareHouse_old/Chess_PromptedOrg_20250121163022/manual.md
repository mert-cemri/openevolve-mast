# Chess Game User Manual

Welcome to the Chess Game application! This manual will guide you through the installation process, introduce you to the main functions of the software, and provide instructions on how to play the game using the Linux Terminal.

## Introduction

The Chess Game application is a terminal-based chess game that allows two players to take turns and determine the winner. The game is designed to be played directly from the Linux Terminal, using standard chess notation for moves.

## Installation

### Prerequisites

Before you can run the Chess Game, ensure that you have the following installed on your system:

- Python 3.x

### Installation Steps

1. **Clone the Repository:**

   Open your terminal and clone the repository using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change your directory to the cloned repository:

   ```bash
   cd <repository-directory>
   ```

   Replace `<repository-directory>` with the name of the cloned directory.

3. **Install Dependencies:**

   The Chess Game application does not require any external dependencies beyond Python 3.x. Ensure Python is installed and accessible from your terminal.

## How to Play

### Starting the Game

To start the game, run the following command in your terminal:

```bash
python main.py
```

### Game Instructions

- **Objective:** The objective of the game is to checkmate your opponent's king.

- **Player Turns:** The game alternates turns between two players: White and Black.

- **Input Moves:** Players enter their moves using standard chess notation. For example, to move a king to e8, type `Ke8`.

- **Game Loop:** The game continues until one player wins by checkmate or the game is manually terminated.

### Input Format

- **Move Notation:** Moves should be entered in the format `<Piece><StartColumn><StartRow><EndColumn><EndRow>`. For example, `Ke8` for moving the king to e8.

- **Valid Pieces:** The pieces are represented by the following characters:
  - King: `K`
  - Queen: `Q`
  - Rook: `R`
  - Bishop: `B`
  - Knight: `N`
  - Pawn: `P`

- **Columns and Rows:** Columns are labeled `a` to `h`, and rows are labeled `1` to `8`.

### Winning the Game

- **Checkmate:** The game ends when a player's king is in checkmate, meaning it cannot escape capture.

- **Declare Winner:** The game will declare the winner once checkmate is achieved.

## Troubleshooting

- **Invalid Input:** If you enter an invalid move or input format, the game will prompt you to try again.

- **Invalid Move:** If a move is not allowed by the rules of chess, the game will notify you and ask for a different move.

## Conclusion

Enjoy playing chess directly from your terminal! If you encounter any issues or have questions, please refer to this manual or contact support for assistance. Happy gaming!