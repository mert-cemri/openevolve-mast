# Strands Puzzle Game

Welcome to the Strands Puzzle Game! This is an engaging word-segmentation puzzle where players combine strands of text to form meaningful words or phrases. The game verifies valid strand formations and confirms completion once all strands are correctly merged.

## Quick Install

To get started with the Strands Puzzle Game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Installation Steps

1. **Clone the Repository:**
   - Clone the repository to your local machine using the following command:
     ```bash
     git clone <repository-url>
     ```

2. **Navigate to the Project Directory:**
   - Change your directory to the project folder:
     ```bash
     cd <project-directory>
     ```

3. **Install Dependencies:**
   - The game requires no additional Python packages beyond the standard library. Ensure your Python environment is set up correctly.

## How to Play

### Running the Game

1. **Prepare Your Files:**
   - Create two text files: one containing the strands and another containing the valid words or phrases.
   - Each line in these files should represent a single strand or valid word/phrase.

2. **Start the Game:**
   - Run the game using the following command:
     ```bash
     python main.py <strands_file> <valid_words_file>
     ```
   - Replace `<strands_file>` with the path to your strands file and `<valid_words_file>` with the path to your valid words file.

### Game Instructions

- **Objective:** Combine the strands to form meaningful words or phrases.
- **Input:** Enter your combination of strands when prompted.
- **Validation:** The game will inform you if your combination is valid.
- **Completion:** The game ends when all valid combinations have been used.

### Example

Suppose you have the following strands in your file:
```
hel
lo
wor
ld
```

And the valid words file contains:
```
hello
world
```

You would enter combinations like `hello` or `world` to complete the puzzle.

## Troubleshooting

- **File Not Found Error:** Ensure the file paths provided are correct and the files exist.
- **Invalid Combination:** If your combination is not recognized, check if it matches any valid words or phrases from your valid words file.

## Documentation

For further assistance and documentation, please refer to the source code comments and docstrings within the Python files. These provide detailed explanations of the functions and classes used in the game.

Enjoy playing the Strands Puzzle Game and challenge your word segmentation skills!