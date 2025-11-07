manual.md

```
# Interactive Storytelling Game

Welcome to the Interactive Storytelling Game, an immersive experience where your decisions shape the narrative and determine your fate. Explore branching storylines, make impactful choices, and discover multiple endings based on your actions.

## 🎮 Overview

This interactive storytelling game presents narrative segments with branching choices. Each decision you make influences subsequent events, character relationships, and items you acquire, ultimately affecting the possible endings. The game tracks your choices and dynamically adjusts the storyline through conditional logic.

## 🚀 Features

- **Interactive Narrative**: Engage with a dynamic story that evolves based on your decisions.
- **Branching Choices**: Multiple paths and outcomes based on player choices.
- **State Tracking**: Manage items and relationships that influence story progression.
- **Conditional Logic**: Choices and outcomes depend on your previous actions and inventory.

## 🛠️ Installation

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

This project requires no external dependencies. However, it's recommended to create a virtual environment for better project management.

### Setting up the Environment

1. **Clone or Download the Project**

   Clone the repository or download the project files to your local machine.

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv storytelling_env
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     storytelling_env\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source storytelling_env/bin/activate
     ```

4. **Install Dependencies**

   Since there are no external dependencies, you can skip this step. If dependencies are added in the future, you can install them using:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ How to Play

### Starting the Game

Navigate to the project directory and run the following command:

```bash
python main.py
```

### Gameplay Instructions

1. **Read the Narrative**: The game will present you with a narrative segment describing your current situation.

2. **Make Choices**: After each narrative segment, you'll be presented with numbered choices. Enter the number corresponding to your desired action and press Enter.

   Example:
   ```
   You wake up in a mysterious forest. What do you do?

   1. Explore the forest
   2. Stay put and wait

   Choose an option: 1
   ```

3. **Progress Through the Story**: Your choices will lead you through different story paths, affecting your inventory and relationships.

4. **Reach an Ending**: Continue making choices until you reach an ending. The game will clearly indicate when you've reached the conclusion of your story.

### Game Mechanics

- **Items**: Certain choices grant you items that can unlock special options later in the story.
- **Relationships**: Interactions with characters can build relationships, influencing future events and outcomes.
- **Conditional Choices**: Some choices will only appear if you meet specific conditions (e.g., possessing an item or having a certain relationship status).

## 📁 Project Structure

```
interactive-storytelling-game/
├── main.py          # Main entry point for the game
├── story.py         # Defines the story structure and logic
├── player.py        # Manages player state (items, relationships)
└── requirements.txt # Lists external dependencies (currently empty)
```

## 📝 Customizing the Story

You can easily customize or expand the story by editing the `story.py` file:

- **Adding New Nodes**: Define new `StoryNode` instances with unique IDs, narrative text, choices, conditions, and effects.
- **Modifying Choices**: Adjust existing choices or add new ones to existing nodes.
- **Conditional Logic**: Set conditions and effects to create more complex and interactive storylines.

Example of adding a new node:

```python
self.nodes['new_adventure'] = StoryNode(
    'new_adventure',
    "You discover a hidden cave. Do you enter?",
    choices=[
        {'text': "Enter the cave", 'next_node': 'cave_entry', 'effects': {'items': ['torch']}},
        {'text': "Walk away", 'next_node': 'walk_away'}
    ]
)
```

## 📞 Support

For any questions, feedback, or issues, please contact our support team or open an issue in the project's repository.

Enjoy your adventure and happy storytelling! 🌟
```