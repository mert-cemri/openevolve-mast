manual.md

```
# 2048 Game

A simple yet addictive puzzle game implemented in Python. Combine tiles with matching numbers to reach higher values and achieve the highest possible score!

## 🎮 What is 2048?

2048 is a popular single-player sliding tile puzzle game played on a 4x4 grid. The objective is to slide numbered tiles on the grid to combine them and create a tile with the number 2048. Each move slides all tiles in one direction (up, down, left, or right). Tiles with the same number merge into one tile with double the value. After each move, a new tile (with a value of 2 or occasionally 4) appears randomly in an empty cell. The game ends when no moves are possible.

## 🚀 Features

- Standard 4x4 grid gameplay.
- Simple keyboard controls (W/A/S/D keys).
- Automatic tile merging and scoring.
- Real-time score tracking.
- Highest tile tracking.
- Game-over detection.

## 🛠️ Installation

### Prerequisites

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This project does not require any external dependencies. All required libraries are part of Python's standard library.

### Setup Instructions

1. Clone or download the project files to your local machine.

2. Navigate to the project directory in your terminal or command prompt.

```bash
cd path/to/your/project
```

3. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

4. Since there are no external dependencies, you can directly run the game.

## ▶️ How to Play

### Starting the Game

Run the following command in your terminal or command prompt:

```bash
python main.py
```

### Controls

Use the following keys to move the tiles:

- **W**: Move tiles up
- **A**: Move tiles left
- **S**: Move tiles down
- **D**: Move tiles right
- **Q**: Quit the game

### Gameplay

- Combine tiles with the same number by sliding them into each other.
- After each move, a new tile (2 or occasionally 4) appears randomly on the grid.
- The game continues until no moves are possible.
- Your current score and the highest tile achieved are displayed after each move.

### Winning the Game

- The standard goal is to reach the 2048 tile, but you can continue playing to achieve even higher tiles and scores.

### Ending the Game

- The game automatically detects when no moves are possible and displays a "Game Over" message along with your final score and highest tile achieved.
- You can also manually quit the game at any time by pressing the **Q** key.

## 📖 Project Structure

```
2048-game/
├── game2048.py  # Core game logic implementation
├── main.py      # Main entry point and user interface
└── requirements.txt  # Dependency file (empty, no external dependencies)
```

## 📌 Example Gameplay

```
Welcome to 2048! Use W/A/S/D keys to move tiles. Press Q to quit.

Score: 0 	Highest Tile: 2
-------------------------
|    .|    .|    .|    2|
-------------------------
|    .|    .|    .|    .|
-------------------------
|    .|    .|    .|    .|
-------------------------
|    .|    .|    2|    .|
-------------------------

Move (W/A/S/D): a
Score: 0 	Highest Tile: 2
-------------------------
|    2|    .|    .|    .|
-------------------------
|    .|    .|    .|    .|
-------------------------
|    .|    .|    .|    .|
-------------------------
|    2|    .|    .|    .|
-------------------------
```

## 📝 License

This project is open-source and available for personal and educational use.

Enjoy playing 2048 and challenge yourself to achieve the highest score possible!
```