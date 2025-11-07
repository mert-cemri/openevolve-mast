```markdown
# Spelling Bee Puzzle Game

Welcome to the Spelling Bee Puzzle Game! This application challenges you to form words using a central letter and six surrounding letters. The goal is to create as many valid words as possible, each including the central letter at least once.

## Main Functions

- **Central and Surrounding Letters**: The game provides one central letter and six surrounding letters. You must use the central letter in every word you form.
- **Word Validation**: Words must be at least four letters long and can only include the provided letters.
- **Scoring System**: Points are awarded based on the length of the word. Each valid word earns points equal to the number of letters minus three.
- **Feedback**: The game provides immediate feedback on the validity of the word you submit.

## Installation

### Environment Setup

To run the Spelling Bee Puzzle Game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Install Dependencies

The game requires the `numpy` library. You can install it using pip:

```bash
pip install numpy==1.21.2
```

Alternatively, you can use the `requirements.txt` file to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the file and executing the following command in your terminal or command prompt:

    ```bash
    python main.py
    ```

2. **Game Interface**: A window will appear displaying the central letter and the surrounding letters. You will also see input fields and buttons for interaction.

3. **Form Words**: Enter a word in the input field and click the "Submit" button. The word must include the central letter and can only use the provided letters.

4. **Receive Feedback**: After submitting a word, you will receive feedback indicating whether the word is valid. If valid, your score will increase based on the word length.

5. **Continue Playing**: Keep forming words to increase your score. The game continues until you decide to stop.

## Troubleshooting

- **GUI Issues**: If you encounter issues with the graphical interface, ensure that your system supports Tkinter and that you have a display available.
- **Dependency Errors**: If you face issues with dependencies, double-check that you have installed the correct version of `numpy` as specified in the `requirements.txt`.

Enjoy the challenge and improve your vocabulary with the Spelling Bee Puzzle Game!
```