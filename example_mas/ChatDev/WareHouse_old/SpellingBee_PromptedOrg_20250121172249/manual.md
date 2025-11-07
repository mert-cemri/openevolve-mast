# Spelling Bee Puzzle Game

Welcome to the Spelling Bee Puzzle Game! This application allows users to engage in a fun and challenging word game where they form words using a central letter and six surrounding letters. The game tracks scores based on word lengths and provides feedback as the user progresses.

## Main Functions

- **Central and Surrounding Letters**: The game starts by allowing the user to input one central letter and six surrounding letters.
- **Word Formation**: Users form words that must include the central letter at least once and can only use the provided letters.
- **Score Tracking**: The game calculates and tracks scores based on the length of valid words.
- **User Feedback**: Provides feedback on the validity of words and displays scores.

## Installation

To run the Spelling Bee Puzzle Game, you need to have Python installed on your system. Follow these steps to set up the environment and dependencies:

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Clone the Repository

Clone the repository containing the game code to your local machine:

```bash
git clone <repository-url>
```

### Step 3: Install Dependencies

Navigate to the project directory and install any required dependencies. If there are any dependencies, they will be listed in a `requirements.txt` file. Use the following command to install them:

```bash
pip install -r requirements.txt
```

### Step 4: Prepare the Valid Words File

Ensure you have a `valid_words.txt` file in the project directory. This file should contain a list of valid words, each on a new line.

## How to Play

1. **Start the Game**: Run the main script to start the game:

   ```bash
   python main.py
   ```

2. **Input Letters**: When prompted, enter the central letter and six surrounding letters. Ensure the surrounding letters are separated by spaces.

3. **Form Words**: Enter words that include the central letter and use only the provided letters. Type 'exit' to quit the game.

4. **Receive Feedback**: The game will validate your word and provide feedback. If the word is valid, you will receive a score based on its length.

5. **Track Your Score**: The game keeps track of your total score as you play.

## Documentation

For more detailed information on the game's architecture and code, refer to the following files:

- `main.py`: Entry point for the application.
- `spelling_bee_game.py`: Manages game logic, including initialization and score tracking.
- `word_validator.py`: Validates words based on game rules.
- `score_tracker.py`: Calculates and tracks scores.
- `user_interface.py`: Manages user interaction and feedback.

Enjoy playing the Spelling Bee Puzzle Game and challenge yourself to form as many valid words as possible!