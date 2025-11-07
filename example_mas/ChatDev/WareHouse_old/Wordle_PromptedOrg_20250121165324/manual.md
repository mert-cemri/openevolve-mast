# Wordle Terminal Game

Welcome to the Wordle Terminal Game! This is a simple and fun word-guessing game that you can play directly from your Linux terminal. The objective is to guess a daily 5-letter English word within six attempts. 

## Main Functions

- **Daily Word Selection**: Each day, a new 5-letter word is randomly selected from a predefined list.
- **Guess Evaluation**: Players have six attempts to guess the word. After each guess, feedback is provided:
  - **Green**: Correct letter in the correct position.
  - **Yellow**: Correct letter in the wrong position.
  - **Grey**: Incorrect letter.
- **Win Condition**: If the player guesses the word correctly within six attempts, they win. Otherwise, the correct word is revealed.

## Installation

To play the Wordle Terminal Game, you need to have Python installed on your Linux system. Follow these steps to set up the game:

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Python**: Ensure you have Python installed. You can check this by running:
   ```bash
   python --version
   ```
   If Python is not installed, you can install it using:
   ```bash
   sudo apt-get update
   sudo apt-get install python3
   ```

3. **Run the Game**: 
   Navigate to the directory where the game files are located and run the main script:
   ```bash
   python3 main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script to start the game. You will be welcomed with a message to guess the 5-letter word.

2. **Enter Your Guess**: Type a 5-letter word and press Enter. The game will evaluate your guess and provide feedback using colors:
   - **Green**: Correct letter in the correct position.
   - **Yellow**: Correct letter in the wrong position.
   - **Grey**: Incorrect letter.

3. **Continue Guessing**: You have a total of six attempts to guess the word correctly. Use the feedback to adjust your guesses.

4. **Win or Lose**: If you guess the word correctly within six attempts, a congratulatory message will be displayed. If not, the correct word will be revealed after the sixth attempt.

## Example

```bash
Welcome to Wordle! Guess the 5-letter word.
Attempt 1/6: apple
a p p l e 
Attempt 2/6: grape
g r a p e 
Attempt 3/6: peach
p e a c h 
Congratulations! You've guessed the word correctly.
```

Enjoy playing the Wordle Terminal Game! If you have any questions or need further assistance, feel free to reach out.