# Puzzle Game User Manual

Welcome to the Puzzle Game! This manual will guide you through the installation, setup, and gameplay of our exciting word puzzle game.

## Introduction

The Puzzle Game is a daily challenge where players must group 16 words into four sets of four, based on hidden categories. The words are presented in a 4x4 grid, and players select four at a time to form a group. Correct groups are removed and revealed with a category and a color-coded difficulty (yellow, green, blue, purple). Incorrect guesses count as mistakes, with a maximum of four allowed. Only one correct solution exists, though words may appear to fit multiple categories. The game includes shuffle functionality and provides immediate feedback after each guess. A new puzzle is generated daily.

## Quick Install

### Prerequisites

- Python 3.x installed on your system.

### Installation Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**

   Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the actual directory name.

3. **Install Dependencies**

   The game does not require any external dependencies, so you can skip this step. However, ensure that your Python environment is set up correctly.

## How to Play

1. **Start the Game**

   Run the main script to start the game:

   ```bash
   python main.py
   ```

2. **Game Interface**

   - The game will display a 4x4 grid of words.
   - You will be prompted to enter your guess by selecting four words that you believe belong to the same category.

3. **Making a Guess**

   - Enter your guess by typing four words separated by spaces.
   - Example: `apple banana orange grape`

4. **Feedback and Progress**

   - If your guess is correct, the words will be removed from the grid, and you will receive feedback indicating the correct category.
   - If your guess is incorrect, you will receive feedback and a mistake will be counted. You have a maximum of four mistakes allowed.

5. **Winning the Game**

   - Successfully group all words into their correct categories to win the game.
   - If you make four mistakes, the game will end, and you will have the option to try again.

6. **Daily Puzzle**

   - A new puzzle is generated daily, providing a fresh challenge each day.

## Additional Features

- **Shuffle Functionality**

  - The words in the grid can be shuffled to provide a different perspective and help you find the correct groups.

## Conclusion

Enjoy the challenge of grouping words into their hidden categories and test your skills with a new puzzle every day. We hope you have a great time playing the Puzzle Game!

For any issues or feedback, please contact our support team.

Happy puzzling!