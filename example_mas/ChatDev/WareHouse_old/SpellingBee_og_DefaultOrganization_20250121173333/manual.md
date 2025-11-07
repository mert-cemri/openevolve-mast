# Spelling Bee Puzzle Game

Welcome to the Spelling Bee Puzzle Game! This application challenges users to form words using a central letter and six surrounding letters. The goal is to create words that include the central letter at least once and only use letters from the provided set. Points are awarded based on the length of the words formed.

## Main Functions

- **Generate Letters**: The game randomly selects one central letter and six surrounding letters from the alphabet.
- **Word Validation**: Users can input words, which are validated to ensure they include the central letter and only use the provided letters.
- **Score Tracking**: The game calculates and displays the score based on the length of valid words submitted by the user.
- **User Interface**: A simple graphical user interface (GUI) allows users to interact with the game easily.

## Installation

To run the Spelling Bee Puzzle Game, you need to have Python installed on your system. Follow these steps to set up the environment and run the game:

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Tkinter**: Tkinter is a standard GUI toolkit in Python. It should be included with your Python installation. If not, you can install it using the following command:
   ```bash
   sudo apt-get install python3-tk
   ```

3. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

4. **Run the Game**: Execute the main application file to start the game.
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` file to launch the game window.

2. **View Letters**: The game will display one central letter and six surrounding letters. Use these letters to form words.

3. **Enter Words**: Type your word into the input field and click the "Submit" button.

4. **Score Points**: If your word is valid, it will be accepted, and your score will increase based on the word's length.

5. **Feedback**: The game provides feedback by updating your score after each valid submission.

6. **Repeat**: Continue forming words to increase your score.

## Additional Information

- **Dictionary**: The game uses a small set of words for validation. In a real application, this can be expanded by loading a comprehensive dictionary file.

- **Feedback and Support**: For any issues or suggestions, please contact our support team.

Enjoy playing the Spelling Bee Puzzle Game and challenge yourself to find as many words as possible!