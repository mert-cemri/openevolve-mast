# Chess Game User Manual

Welcome to the Chess Game application! This manual will guide you through the installation, setup, and usage of the chess game designed to be played from the Linux Terminal. This game allows two players to take turns and determine the winner based on standard chess rules.

## Quick Install

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the Repository:**

   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   ```bash
   cd <repository-directory>
   ```

   Replace `<repository-directory>` with the name of the cloned repository.

3. **Install Dependencies:**

   This project does not require any external dependencies, so you can skip this step.

## How to Play

### Starting the Game

1. **Run the Game:**

   In the terminal, execute the following command to start the game:

   ```bash
   python main.py
   ```

2. **Game Interface:**

   - The game will display the chessboard in the terminal.
   - Players will take turns to make moves.
   - The current player's color will be displayed, indicating whose turn it is.

### Making Moves

- **Input Format:**

  Players should enter their moves using standard chess notation. For example, to move a piece from e2 to e4, type:

  ```bash
  e2e4
  ```

- **Invalid Moves:**

  If an invalid move is entered, the game will prompt you to try again.

### Winning the Game

- The game will automatically check for checkmate, stalemate, and draw conditions.
- The game ends when a player wins by checkmate or if a stalemate/draw is reached.

## Main Functions of the Software

- **ChessGame Class:**

  - Manages the overall game flow, including initializing the board, switching turns, and checking for a winner.

- **Board Class:**

  - Represents the chessboard and manages piece movements and board state.

- **Player Class:**

  - Represents a player and handles move input.

- **Piece Class:**

  - Represents individual chess pieces and their possible moves.

- **Move Class:**

  - Parses and validates moves according to chess rules.

## Additional Information

- The game is designed to be played in a terminal environment, providing a simple and straightforward chess experience without a graphical user interface.
- Future updates may include more advanced features such as move validation for each piece type and enhanced checkmate/stalemate detection.

Enjoy playing chess in your terminal! If you encounter any issues or have suggestions for improvements, please feel free to contribute to the project or contact the development team.