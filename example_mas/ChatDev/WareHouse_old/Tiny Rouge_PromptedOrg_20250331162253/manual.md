# Roguelike Game Inspired by Tower of the Sorcerer

Welcome to the user manual for our roguelike game, inspired by the classic "Tower of the Sorcerer". This guide will walk you through the main features of the game, how to set up your environment, and how to play the game.

## Game Overview

This roguelike game is set on a fixed 80x80 grid map. The player character is controlled using the W/A/S/D keys for movement (up, left, down, right). The objective is to navigate through the map, avoiding or defeating monsters, collecting treasures, and ultimately reaching the door to proceed to the next level. The game ensures there is always at least one valid path from the starting position to the door.

### Main Features

- **Grid Map**: Navigate through an 80x80 grid map filled with walls, floor tiles, monsters, and treasures.
- **Player Movement**: Use W/A/S/D keys to move the player character on floor tiles.
- **Combat System**: Engage in combat with monsters by subtracting their HP from the player's HP.
- **Treasure Collection**: Restore the player's HP by 20–30 points when touching a treasure chest.
- **Minimal UI**: Display the player's current HP and encountered monster stats.

## Installation

### Environment Setup

This project does not require any external dependencies, making it easy to set up and run. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Start by cloning the repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Move into the project directory.
   ```bash
   cd <project-directory>
   ```

3. **Run the Game**: Execute the main Python script to start the game.
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script to begin your adventure.

2. **Control the Player**: Use the following keys to move your character:
   - `W`: Move up
   - `A`: Move left
   - `S`: Move down
   - `D`: Move right

3. **Navigate the Map**: Move through the grid, avoiding walls and finding the path to the exit.

4. **Encounter Monsters**: When you encounter a monster, your HP will decrease by the monster's HP. Be strategic in your movements to preserve your health.

5. **Collect Treasures**: Increase your HP by 20–30 points by collecting treasures scattered across the map.

6. **Reach the Exit**: Your goal is to reach the door at the end of the map to proceed to the next level.

7. **Monitor Your Stats**: Keep an eye on your current HP and any monster encounters through the minimal UI display.

## Conclusion

We hope you enjoy playing this roguelike game and navigating through its challenges. If you have any questions or need further assistance, please feel free to reach out to our support team. Happy gaming!