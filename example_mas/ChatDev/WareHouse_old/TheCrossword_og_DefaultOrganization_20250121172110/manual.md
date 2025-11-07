# Crossword Puzzle Application

Welcome to the Crossword Puzzle Application! This application allows you to engage in the classic crossword puzzle game, where you can fill in words based on given clues. The application validates your entries and confirms completion when all correct words are filled in.

## Main Functions

The Crossword Puzzle Application provides the following main functions:

1. **Grid Display**: A grid of squares is displayed where you can enter letters to form words.
2. **Clue Management**: Clues for both across and down entries are provided to guide you in filling the grid.
3. **Word Entry**: You can enter words by specifying the clue number and direction.
4. **Validation**: The application checks if the entered letters match the correct words.
5. **Completion Confirmation**: The application confirms when all correct words are filled in, signaling the completion of the puzzle.

## Installation

To run the Crossword Puzzle Application, you need to set up your environment with the necessary dependencies. Follow these steps to install the required packages:

1. **Python Installation**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Use the following command to install the required dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `pyvirtualdisplay` package, which is necessary for running the application in environments without a display.

## How to Use

1. **Launch the Application**: Run the `main.py` script to start the application. You can do this by executing the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Interact with the Grid**: Once the application is running, you will see a grid of squares. Each square represents a letter in the crossword puzzle.

3. **View Clues**: A list of clues is displayed below the grid. Each clue is associated with a number and a direction (across or down).

4. **Enter Words**:
   - Select a clue from the list by clicking on it.
   - Enter the corresponding word in the text entry box provided.
   - Click the "Submit Word" button to validate and fill the word in the grid.

5. **Check Solution**: After filling in all the words, click the "Check" button to verify if the crossword is complete. If all words are correct, a success message will be displayed.

6. **Completion**: Once the crossword is successfully completed, you will receive a congratulatory message.

Enjoy solving the crossword puzzle and challenge yourself with the clues provided! If you encounter any issues or have questions, feel free to reach out for support. Happy puzzling!