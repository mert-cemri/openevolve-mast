```markdown
# Adventure CLI Game Engine

Welcome to the Adventure CLI Game Engine! This software allows you to create and play a simple text-based adventure game using a command-line interface. The game data, including rooms, descriptions, items, and choices, is loaded from a JSON or YAML file, providing flexibility and ease of customization.

## Main Features

- **Text-Based Adventure**: Navigate through different rooms by typing commands.
- **Customizable Game Data**: Load game data from JSON or YAML files to define rooms, items, and navigation choices.
- **Simple CLI Interface**: Interact with the game using a straightforward command-line interface.
- **Optional GUI**: A basic GUI using Tkinter is available for a visual representation of the game.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Quick Install

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the required Python packages.
   ```bash
   pip install -r requirements.txt
   ```

   *(Note: If a `requirements.txt` file is not provided, ensure you have the following packages installed: `tkinter` for GUI support, though it is optional.)*

## How to Play

1. **Run the Game**: Start the game by executing the `main.py` script.
   ```bash
   python main.py
   ```

2. **Navigate the Game**: Use text commands to navigate through the game. The available commands will be based on the current room's choices.

3. **Game Commands**:
   - **Movement**: Type the direction you want to move (e.g., `north`, `south`, `east`, `west`).
   - **Invalid Commands**: If you enter an invalid command, the game will prompt you with available options.

4. **End the Game**: To exit the game, you can simply close the terminal or use a keyboard interrupt (Ctrl+C).

## Customizing the Game

- **Game Data**: Modify the `game_data.json` file to customize the rooms, descriptions, items, and choices. You can also create a YAML file if preferred.

- **Adding Rooms**: Add new rooms by defining their name, description, items, and choices in the game data file.

- **Items and Choices**: Customize the items available in each room and the choices for navigation.

## Optional GUI

For a graphical interface, you can use the optional GUI provided in `gui.py`. To run the GUI version, execute the following command:

```bash
python gui.py
```

## Documentation

For further details on how to extend or modify the game engine, please refer to the source code documentation within each module.

Enjoy your adventure!
```
