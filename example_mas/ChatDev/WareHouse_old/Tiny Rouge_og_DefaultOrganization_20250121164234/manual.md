# Tower of the Sorcerer: Roguelike Game

Welcome to the Tower of the Sorcerer, a roguelike game inspired by classic dungeon crawlers. Navigate through the treacherous tower, battling monsters, collecting treasures, and advancing to the next level through strategic gameplay.

## Main Features

- **Map Exploration**: Navigate an 80x80 grid map using keyboard controls.
- **Character Movement**: Use W/S/A/D keys to move your character up, down, left, and right.
- **Combat System**: Engage with monsters, where your health points (HP) are compared to the monster's HP to determine the outcome.
- **Treasure Collection**: Restore your HP by collecting treasure chests, which randomly restore 20-30 HP.
- **Level Advancement**: Progress to the next level by reaching the door.
- **Pathfinding**: Ensure there is always a path from the starting position to the door.

## Installation

To get started with the Tower of the Sorcerer game, follow these steps to set up your environment:

### Prerequisites

- Python 3.x installed on your system.
- `pip` package manager for Python.

### Quick Install

1. **Clone the Repository**: Download the game code from the repository.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use the following command to install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `pygame` library, which is necessary for running the game.

## How to Play

1. **Start the Game**: Run the main game script to start playing.

   ```bash
   python main.py
   ```

2. **Game Controls**:
   - Use `W` to move up.
   - Use `S` to move down.
   - Use `A` to move left.
   - Use `D` to move right.

3. **Game Objectives**:
   - Navigate through the map and find the door to advance to the next level.
   - Engage with monsters strategically, as your HP will decrease based on the monster's HP.
   - Collect treasure chests to restore your HP and increase your chances of survival.

4. **Game Environment**:
   - The map consists of walls, floors, monsters, treasure chests, and doors.
   - You cannot pass through walls, so plan your path carefully.
   - Ensure you find the path from the starting position to the door to progress.

## Troubleshooting

- **Game Not Starting**: Ensure that all dependencies are installed correctly. Re-run `pip install -r requirements.txt` if necessary.
- **Performance Issues**: Make sure your system meets the minimum requirements for running Python and `pygame`.

## Additional Resources

For more information on the game mechanics and updates, please refer to the documentation provided in the repository or contact our support team.

Enjoy your adventure in the Tower of the Sorcerer!