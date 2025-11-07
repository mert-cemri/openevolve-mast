# Tower of the Sorcerer Roguelike Game

Welcome to the Tower of the Sorcerer Roguelike Game, a thrilling adventure where you navigate through a mysterious tower filled with monsters, treasures, and challenges. This game is inspired by classic roguelike games and offers an engaging experience with strategic gameplay.

## Main Functions

- **Player Movement**: Use the keyboard keys W, A, S, D to control the player character. Navigate through the tower by moving up, down, left, and right.
- **Monsters**: Encounter monsters that will challenge your progress. Your HP will decrease based on the monster's HP when attacked.
- **Treasure Chests**: Discover treasure chests that restore your HP by a random amount between 20 and 30.
- **Doors**: Reach the door to proceed to the next level of the tower.
- **Map**: Explore an 80x80 grid map with a guaranteed path from the starting position to the door.

## Installation

### Environment Setup

1. **Python Version**: Ensure you have Python 3.8 or higher installed on your system.

2. **Clone the Repository**: Download the game code from the repository.

3. **Install Dependencies**: Although there are no external dependencies required, ensure your Python environment is set up correctly.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Requirements**: Install any necessary packages (if specified in the future).

   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game.

   ```bash
   python main.py
   ```

2. **Game Controls**: Use the following keys to control your character:
   - `W`: Move up
   - `A`: Move left
   - `S`: Move down
   - `D`: Move right

3. **Game Objective**: Navigate through the map, avoid or defeat monsters, collect treasures, and reach the door to advance to the next level.

4. **Game Map**: The map is displayed in the console with the following symbols:
   - `P`: Player
   - `M`: Monster
   - `T`: Treasure Chest
   - `D`: Door
   - `.`: Floor

5. **Interactions**:
   - **Monsters**: When you encounter a monster, your HP will decrease by the monster's HP.
   - **Treasure Chests**: Open treasure chests to restore your HP.
   - **Doors**: Reach the door to proceed to the next level.

## Additional Information

This game is a simple yet engaging roguelike experience designed to test your strategic thinking and navigation skills. As you progress through the levels, the challenges will increase, requiring careful planning and resource management.

Enjoy your adventure in the Tower of the Sorcerer!