```markdown
# Interactive Storytelling Game

Welcome to the Interactive Storytelling Game, an engaging application where your choices shape the narrative and lead to different outcomes. This user manual will guide you through the installation, features, and gameplay of the application.

## Quick Install

To get started with the Interactive Storytelling Game, ensure you have Python installed on your system. The game does not require any external dependencies, making the setup straightforward.

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game:**
   ```bash
   python main.py
   ```

## 🤔 What is this?

The Interactive Storytelling Game is a narrative-driven application where players make choices that influence the story's progression and outcome. The game tracks variables such as relationships and items, allowing for multiple endings based on player decisions.

### Main Features

- **Narrative Segments:** Experience a rich storyline with various narrative segments.
- **Branching Choices:** Make decisions that branch the story into different paths.
- **Dynamic Outcomes:** Your choices affect relationships, items, and the story's ending.
- **Graphical User Interface (GUI):** Enjoy an intuitive interface powered by Tkinter.
- **Command-Line Interface (CLI):** Play the game in a text-based environment if GUI is not available.

## 📖 How to Play

### Starting the Game

- **GUI Mode:** If you have a graphical display, the game will launch in GUI mode by default. You will see the story text and buttons for each choice.
- **CLI Mode:** If no display is detected, the game will run in CLI mode, where you will interact with the game via text input.

### Making Choices

- **GUI Mode:** Click on the buttons corresponding to your choice to progress the story.
- **CLI Mode:** Type your choice and press Enter to continue.

### Tracking Progress

- The game automatically tracks your relationships and items based on your decisions. These variables influence the story's direction and possible endings.

### Ending the Game

- The game concludes when you reach a narrative endpoint. You can restart the game to explore different paths and outcomes.

## Additional Information

- **Story Nodes:** The story is structured in nodes, each representing a segment with text and choices. These nodes are defined in the `story_nodes.json` file.
- **Customization:** You can modify the story by editing the `story_nodes.json` file to add new segments and choices.

Enjoy exploring the myriad possibilities within the Interactive Storytelling Game, where every decision shapes your adventure!
```
