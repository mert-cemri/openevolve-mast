# Tower of the Sorcerer Game

Welcome to the Tower of the Sorcerer, a roguelike game inspired by classic dungeon crawlers. Navigate through a mysterious tower filled with monsters, treasure chests, and doors leading to new levels. Your goal is to survive, collect treasures, and reach the top of the tower.

## Main Functions

- **Player Movement**: Use the keyboard keys W, A, S, D to move your character up, left, down, and right respectively.
- **Interacting with the Environment**:
  - **Monsters**: Encountering a monster will result in a battle where your HP is reduced by the monster's HP.
  - **Treasure Chests**: Open treasure chests to restore 20-30 HP randomly.
  - **Doors**: Reach the door to advance to the next level.
- **Game Map**: The game map is an 80x80 grid with floors, walls, monsters, chests, and doors. You cannot pass through walls, ensuring a strategic pathfinding experience.

## Installation

### Environment Setup

To run the game, you need to have Python and the necessary dependencies installed on your system. Follow these steps to set up your environment:

1. **Install Python**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Pygame**: Pygame is required to run the game. Install it using pip:

   ```bash
   pip install pygame==2.1.2
   ```

3. **Clone the Repository**: Clone the game repository to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

4. **Install Dependencies**: Ensure all dependencies are installed by running:

   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**: Navigate to the directory where the game files are located and run the main game script:

   ```bash
   python main.py
   ```

2. **Game Controls**:
   - **W**: Move up
   - **A**: Move left
   - **S**: Move down
   - **D**: Move right

3. **Objective**: Navigate through the levels, defeat monsters, collect treasures, and find the door to advance to the next level.

4. **Game Over**: The game ends when your HP reaches zero. Try to maintain your health by avoiding unnecessary battles and collecting treasures.

## Additional Information

- **Game Design**: The game uses a procedural generation algorithm to create a maze-like map ensuring at least one path from the starting position to the door.
- **Graphics**: The game uses simple 2D graphics to represent different elements like floors, walls, monsters, chests, and doors.

Enjoy your adventure in the Tower of the Sorcerer!