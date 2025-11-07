# ChatDev Text-Based Adventure Game CLI Engine

## Introduction

Welcome to the ChatDev Text-Based Adventure Game CLI Engine! This is a simple yet powerful command-line interface (CLI) application designed to bring the joy of text-based adventure games to your terminal. The game engine is built in Python and can load game data from either JSON or YAML files, allowing for easy customization and expansion.

## Main Features

- **Dynamic Game Data Loading**: Load game data from JSON or YAML files, making it easy to create and modify game scenarios.
- **Interactive Navigation**: Navigate through rooms, pick up items, and make choices using simple text commands.
- **Help System**: Get assistance with available commands by typing `help` at any time during the game.

## Quick Install

To get started with the ChatDev Text-Based Adventure Game CLI Engine, you'll need to have Python installed on your system. We recommend using Python 3.6 or later.

### Step 1: Install Python

If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Required Dependencies

The project requires the `PyYAML` library to parse YAML files. You can install it using `pip`:

```bash
pip install pyyaml
```

Alternatively, you can use the `requirements.txt` file provided in the project directory:

```bash
pip install -r requirements.txt
```

## How to Use the Game

### Step 1: Prepare Game Data

The game engine loads game data from a JSON or YAML file. You can use the provided `data.json` or `data.yaml` files as a starting point or create your own.

Here's an example of a simple game data file in JSON format:

```json
{
    "start_room": "hall",
    "rooms": [
        {
            "name": "hall",
            "description": "You are in a long hall with doors to the north and east.",
            "choices": {
                "north": "kitchen",
                "east": "dining room"
            }
        },
        {
            "name": "kitchen",
            "description": "You are in a cozy kitchen with a wooden table.",
            "items": ["key"],
            "choices": {
                "south": "hall"
            }
        },
        {
            "name": "dining room",
            "description": "You are in a dining room with a large table.",
            "choices": {
                "west": "hall"
            }
        }
    ]
}
```

### Step 2: Run the Game

Navigate to the project directory in your terminal and run the following command:

```bash
python main.py
```

This will start the game engine and load the game data from `data.json`. If you want to use a YAML file, simply change the filename in the `main.py` script:

```python
game_data = data_loader.load_game_data('data.yaml')
```

### Step 3: Play the Game

Once the game starts, you'll see a welcome message and the description of the starting room. You can navigate through the game by typing commands. Here are some available commands:

- `go <direction>`: Move in a specified direction (e.g., `go north`).
- `take <item>`: Pick up an item from the current room (e.g., `take key`).
- `quit`: Exit the game.
- `help`: Show a list of available commands.

## Customizing the Game

To create your own game scenarios, you can modify the game data file. Here are some tips:

- **Rooms**: Define rooms with unique names, descriptions, items, and choices.
- **Items**: Add items to rooms that the player can pick up.
- **Choices**: Specify possible directions the player can move from each room.

## Conclusion

We hope you enjoy playing the ChatDev Text-Based Adventure Game CLI Engine! If you have any questions or suggestions, feel free to reach out to us. Happy adventuring!

---

This manual should provide a comprehensive guide for users to understand, install, and play the game. Let me know if you need any further adjustments or additional information!