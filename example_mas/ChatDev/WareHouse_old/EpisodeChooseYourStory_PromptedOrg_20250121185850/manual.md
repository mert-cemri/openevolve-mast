```markdown
# Interactive Storytelling Game

Welcome to the Interactive Storytelling Game! This application allows players to immerse themselves in a narrative-driven experience where their choices influence the story's progression and outcome. 

## Main Functions

- **Narrative Segments**: The game presents players with narrative segments that set the scene and provide context for decision-making.
- **Branching Choices**: Players are given choices that determine the direction of the story.
- **Dynamic Story Progression**: Player decisions influence subsequent story events, leading to different paths and endings.
- **Variable Tracking**: The game tracks variables such as relationships and items, which can alter possible endings.

## Installation

To run the Interactive Storytelling Game, you need to have Python installed on your system. Follow the steps below to set up the environment and dependencies:

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for your project to manage dependencies. Run the following commands in your terminal or command prompt:

```bash
# Create a virtual environment
python -m venv storytelling_env

# Activate the virtual environment
# On Windows
storytelling_env\Scripts\activate

# On macOS/Linux
source storytelling_env/bin/activate
```

### Step 3: Install Dependencies

Navigate to the project directory and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

(Note: Ensure that a `requirements.txt` file is present in the project directory with necessary dependencies listed. If not, you may need to manually install any additional libraries used in the code.)

## How to Play

Once the environment is set up, you can start the game by running the `main.py` script. Follow these steps:

1. **Navigate to the Project Directory**: Open your terminal or command prompt and navigate to the directory where the game files are located.

2. **Run the Game**: Execute the following command to start the game:

   ```bash
   python main.py
   ```

3. **Interact with the Game**: The game will present you with narrative segments and choices. Type your choice when prompted and press Enter to proceed.

4. **Experience Different Outcomes**: Your choices will influence the story's direction and outcome. Explore different paths by making different decisions.

## Additional Information

- **Story Structure**: The story is managed by the `StoryManager` class, which loads and progresses the story based on player choices.
- **Player Data**: The `Player` class tracks relationships and items, which can affect the story's progression and endings.
- **Utilities**: The `utilities.py` module provides helper functions, such as `print_with_delay`, to enhance the storytelling experience.

Enjoy your journey through the Interactive Storytelling Game, where every choice matters!
```