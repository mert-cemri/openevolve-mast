manual.md

```
# Score Comparison Software

This software provides a simple function to compare two lists of scores and guesses, returning a list of the absolute differences between each pair of corresponding elements. It is designed to help users determine how accurate their guesses were compared to actual results.

## Main Functionality

The core functionality of this software is encapsulated in the `compare` function. This function takes two lists as input: one representing the actual scores of a series of matches, and the other representing the guessed scores. It returns a list of the same length, where each element is the absolute difference between the corresponding elements of the input lists. If a guess is correct, the difference is 0.

### Example Usage

```python
from main import compare

# Example 1
actual_scores = [1, 2, 3, 4, 5, 1]
guessed_scores = [1, 2, 3, 4, 2, -2]
result = compare(actual_scores, guessed_scores)
print(result)  # Output: [0, 0, 0, 0, 3, 3]

# Example 2
actual_scores = [0, 5, 0, 0, 0, 4]
guessed_scores = [4, 1, 1, 0, 0, -2]
result = compare(actual_scores, guessed_scores)
print(result)  # Output: [4, 4, 1, 0, 0, 6]
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. Clone the repository or download the `main.py` file to your local machine.
2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
3. No additional installation steps are required as there are no external dependencies.

## How to Use

1. Open your Python environment (e.g., terminal, command prompt, or an IDE like PyCharm or VSCode).
2. Import the `compare` function from the `main.py` file.
3. Prepare your lists of actual scores and guessed scores.
4. Call the `compare` function with these lists as arguments.
5. Analyze the output list to see how accurate the guesses were.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is well-documented to assist you in understanding its usage and functionality.

```