# Word Categorization Puzzle Game

Welcome to the Word Categorization Puzzle Game, a fun and interactive application where you can challenge your categorization skills by grouping words into their correct categories. This game is inspired by the NYT Connections game and is designed to provide an engaging experience for users of all ages.

## Main Functions

The Word Categorization Puzzle Game offers the following main functions:

- **Word Grouping:** Users must group sixteen words into four categories of four words each.
- **Feedback System:** After each guess, the game provides feedback on whether the chosen words form a valid group.
- **Game Completion:** The game ends when the user successfully forms all four correct groups or runs out of tries.

## Installation

### Environment Setup

This application is developed in Python and requires a Python environment to run. Follow these steps to set up your environment:

1. **Install Python:** Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository:** Clone the project repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory:**
   ```bash
   cd <project-directory>
   ```

4. **Install Dependencies:** Although this project does not require any external dependencies, ensure your environment is set up correctly. You can create a virtual environment to manage your Python packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

5. **Install Required Packages:** There are no external dependencies required for this project, as indicated in the `requirements.txt` file.

## How to Play

1. **Start the Game:** Run the main application script to start the game:
   ```bash
   python main.py
   ```

2. **Game Interface:** The game will launch a graphical user interface (GUI) where you will see buttons representing each word.

3. **Select Words:** Click on the buttons to select words you believe belong to the same category. You must select exactly four words before submitting your guess.

4. **Submit Your Guess:** Once you have selected four words, click the "Submit" button to check if your selection forms a valid group.

5. **Receive Feedback:** The game will inform you if your selected words form a correct group. If correct, those words will be disabled, and you can continue to find the remaining groups.

6. **Game Over:** The game ends when you successfully find all four groups or run out of tries. You will receive a congratulatory message if you complete the game or a message encouraging you to try again if you run out of tries.

Enjoy the challenge and have fun categorizing words in this engaging puzzle game!