```markdown
# NYT Strands Puzzle Game

Welcome to the NYT Strands Puzzle Game! This interactive application allows players to connect word segments to form valid words or phrases. Each connected segment should produce a meaningful solution, and players receive immediate feedback on their selections.

## Main Functions

- **Interactive Gameplay**: Players can select word segments to form valid phrases. The game provides immediate feedback on whether the selected segments form a correct solution.
- **User Interface**: The game features a simple graphical user interface (GUI) using Tkinter, making it easy to navigate and play.
- **Word Segments**: The game includes a set of predefined word segments that players can connect to form valid phrases.

## Installation

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: This project does not require any external dependencies, as indicated in the `requirements.txt` file. However, ensure Tkinter is available in your Python environment. Tkinter is included with standard Python installations on most systems.

3. **Run the Application**: Execute the main application file to start the game.
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Launch the application by running `main.py`. A window will open displaying the available word segments.

2. **Select Word Segments**: Click on the buttons representing word segments to select them. The selected segments will be displayed in the order of selection.

3. **Form Valid Phrases**: Try to connect the segments to form valid phrases. The game will provide feedback:
   - **Correct!**: If the selected segments form a valid phrase, you will receive a "Correct!" message, and the selection will be cleared for a new attempt.
   - **Try again.**: If the segments do not form a valid phrase, you will receive a "Try again." message, and you can continue selecting segments.

4. **Repeat**: Continue playing by forming different valid phrases from the available segments.

## Additional Information

- **Valid Phrases**: The game currently recognizes the following valid phrases: "hello world", "python code", and "open source".
- **Customization**: You can customize the word segments and valid phrases by modifying the `game_logic.py` file.

Enjoy playing the NYT Strands Puzzle Game and challenge yourself to form all the valid phrases!
```