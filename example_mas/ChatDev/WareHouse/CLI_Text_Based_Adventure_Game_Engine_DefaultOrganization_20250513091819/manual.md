# Adventure Game CLI Engine

Welcome to the Adventure Game CLI Engine! This software allows you to experience a simple text-based adventure game where you can explore rooms, collect items, and navigate through a virtual world using command-line inputs.

## Main Functions

The Adventure Game CLI Engine provides the following main functions:

- **Explore Rooms**: Navigate through different rooms by typing commands like "go north" or "go east".
- **Collect Items**: Pick up items found in rooms by using commands like "take torch".
- **Inventory Management**: View the items you have collected using the "inventory" command.
- **Game Data Loading**: Load game data such as rooms, descriptions, items, and choices from a JSON file.

## Installation

To run the Adventure Game CLI Engine, you need to have Python installed on your system. Follow these steps to set up the environment and run the game:

1. **Install Python**: Ensure that Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Download or clone the repository containing the game code.

3. **Install Dependencies**: Navigate to the directory containing the game files and install any required dependencies. This game does not require any external Python packages, so you can skip this step.

4. **Prepare Game Data**: Ensure that the `game_data.json` file is present in the same directory as the game scripts. This file contains the game data needed to run the game.

## How to Play

1. **Start the Game**: Open a terminal or command prompt, navigate to the directory containing the game files, and run the following command:

   ```bash
   python main.py
   ```

2. **Game Commands**: Once the game starts, you can use the following commands to interact with the game:

   - **Move Between Rooms**: Use commands like `go north`, `go south`, `go east`, or `go west` to move between rooms.
   - **Take Items**: Use the command `take [item_name]` to pick up items in the current room. For example, `take torch`.
   - **Check Inventory**: Use the command `inventory` to view the items you have collected.
   - **Exit the Game**: Type `quit` or `exit` to end the game session.

3. **Game Objective**: Explore the rooms, collect items, and enjoy the adventure! The game ends when you decide to quit.

## Example Gameplay

Here's an example of how a typical game session might look:

```
Welcome to the Adventure Game!
You are at the entrance of a dark cave.
> go north
You move to the Hallway.
A narrow hallway with flickering lights.
> go east
You move to the Treasure Room.
A room filled with treasures.
> take gold coin
You take the gold coin.
> inventory
You have the following items:
- gold coin: A shiny gold coin.
> quit
Thanks for playing!
```

Enjoy your adventure and have fun exploring the virtual world! If you encounter any issues or have questions, feel free to reach out for support.