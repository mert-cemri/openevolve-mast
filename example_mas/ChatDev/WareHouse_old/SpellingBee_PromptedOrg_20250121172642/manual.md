# Spelling Bee Game

Welcome to the Spelling Bee Game! This application allows users to engage in a fun and challenging word puzzle where they must form words using a central letter and a set of surrounding letters. The game tracks the score based on word lengths and provides feedback as the user progresses.

## Main Functions

- **Central and Surrounding Letters**: The game provides one central letter and six surrounding letters. Users must form words that include the central letter at least once and only use letters from the provided set.
- **Word Validation**: The game checks if the entered word is valid, ensuring it meets the criteria of containing the central letter and using only the allowed letters.
- **Scoring System**: The score is calculated based on the length of the word, with bonus points for words that are seven letters or longer.
- **Feedback**: The game provides feedback on the validity of the word and displays the current score and number of words found.

## Quick Install

To get started with the Spelling Bee Game, you need to have Python installed on your system. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

*Note: Ensure you have Python and pip installed on your system before running the above command.*

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Game Instructions**: Once the game starts, you will see the central letter and the surrounding letters displayed on the screen.

3. **Enter Words**: Type a word that includes the central letter and only uses the provided letters. Press Enter to submit the word.

4. **Receive Feedback**: After submitting a word, you will receive feedback indicating whether the word is accepted or not. The game will also display the current score and the number of words found.

5. **Exit the Game**: Type 'exit' and press Enter to quit the game.

6. **Final Score**: Upon exiting, the game will display your final score.

## Example

Here's an example of how the game interaction might look:

```
Welcome to the Spelling Bee Game!
Central Letter: e
Surrounding Letters: a, b, c, d, f, g

Enter a word (or 'exit' to quit): face
Good job! Word accepted.
Words found: 1, Score: 4

Enter a word (or 'exit' to quit): bead
Word does not contain the central letter.
Words found: 1, Score: 4

Enter a word (or 'exit' to quit): badge
Good job! Word accepted.
Words found: 2, Score: 9

Enter a word (or 'exit' to quit): exit
Thanks for playing! Final Score: 9
```

Enjoy playing the Spelling Bee Game and challenge yourself to find as many words as possible!