```markdown
# Tower of the Sorcerer Roguelike Game

Welcome to the Tower of the Sorcerer Roguelike Game! This game is inspired by classic roguelike games and features a procedurally generated map where you control a character navigating through levels filled with monsters, treasure chests, and a door to the next level.

## Main Functions

- **Character Movement**: Use keyboard keys W/S/A/D to control the player character up, down, left, and right.
- **Level Progression**: Reach the door to proceed to the next level.
- **Combat and Health**: Encounter monsters and adjust your health based on combat outcomes.
- **Treasure Chests**: Restore health by finding and interacting with treasure chests.
- **Map Generation**: Each level is a new 80x80 grid with a guaranteed path from start to door.

## Installation

This game is implemented in Python and does not require any external dependencies. To get started, ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the game repository to your local machine.
2. **Navigate to the Game Directory**: Open a terminal and navigate to the directory containing the game files.
3. **Run the Game**: Execute the following command to start the game:

   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the game using the command above. The game will initialize and display the map.
2. **Control the Character**: Use the following keys to move your character:
   - `W`: Move up
   - `S`: Move down
   - `A`: Move left
   - `D`: Move right
3. **Interact with the Map**: As you move, you may encounter:
   - **Monsters**: Combat occurs automatically, and your health will be adjusted.
   - **Treasure Chests**: Interact to restore a random amount of health (20-30 HP).
   - **Walls**: Cannot be passed through.
   - **Door**: Reach the door to complete the level and proceed to the next.
4. **Complete Levels**: The objective is to reach the door on each level. The game will automatically generate a new map for each level.

## Game Elements

- **Player**: Starts with 100 HP and can move across the map.
- **Monsters**: Have varying HP and will reduce the player's HP upon interaction.
- **Treasure Chests**: Restore a random amount of HP when interacted with.
- **Door**: The goal of each level, leading to the next.

Enjoy exploring the Tower of the Sorcerer and overcoming its challenges!

```
