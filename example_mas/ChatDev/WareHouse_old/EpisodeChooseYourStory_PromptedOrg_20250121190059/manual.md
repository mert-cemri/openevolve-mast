# Interactive Storytelling Game

Welcome to the Interactive Storytelling Game, an engaging application where your choices shape the narrative and lead to different outcomes. This user manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to play the game.

## Quick Install

To get started with the Interactive Storytelling Game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Step-by-step Installation

1. **Clone the Repository:**
   Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**
   Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies:**
   The game requires certain Python packages. Install them using pip:
   ```bash
   pip install -r requirements.txt
   ```
   Note: Ensure you have a `requirements.txt` file listing all necessary dependencies. If not, you may need to manually install packages like `pytest` for testing, if applicable.

## Main Functions

The Interactive Storytelling Game is designed to provide an immersive experience where player decisions influence the story's progression and outcome. Here are the main components:

- **StoryManager:** Manages the loading and retrieval of story segments.
- **PlayerState:** Tracks the player's state, including relationships and items that affect the story's ending.
- **StorySegment:** Represents a segment of the story with narrative and choices.
- **Choice:** Represents a decision point in the story, affecting the player's state and leading to different segments.

## How to Play

1. **Start the Game:**
   Run the main script to start the game:
   ```bash
   python main.py
   ```

2. **Make Choices:**
   As the story unfolds, you will be presented with narrative segments and choices. Each choice will have a description and will lead to different story paths. Make your selection by entering the corresponding number.

3. **Track Your Progress:**
   Your decisions will affect your player state, which includes variables like friendship, wealth, and caution. These variables will influence the possible endings of your story.

4. **Determine Your Ending:**
   At the end of the game, your accumulated state will determine the outcome of your journey. Whether you end with companionship, wealth, or unchanged, each playthrough offers a unique experience.

## Conclusion

Enjoy the adventure and explore the various paths and endings the Interactive Storytelling Game has to offer. Your choices shape the narrative, making each playthrough a unique experience. Happy storytelling!