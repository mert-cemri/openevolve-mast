manual.md

```
# Score Guess Comparison Tool

This software provides a simple function to compare two lists: one containing actual scores and the other containing guessed scores. The function calculates the difference between each pair of actual and guessed scores, indicating how far off each guess was. This tool is useful for evaluating the accuracy of predictions in various contexts, such as sports matches or other competitive events.

## Main Functionality

The core functionality of this software is encapsulated in the `compare` function. This function takes two lists of equal length as input: `game` (actual scores) and `guess` (guessed scores). It returns a list of the same length, where each element represents the absolute difference between the corresponding elements in the `game` and `guess` lists. If a guess is correct, the difference is 0.

### Example Usage

```python
from main import compare

# Example 1
actual_scores = [1, 2, 3, 4, 5, 1]
guessed_scores = [1, 2, 3, 4, 2, -2]
differences = compare(actual_scores, guessed_scores)
print(differences)  # Output: [0, 0, 0, 0, 3, 3]

# Example 2
actual_scores = [0, 5, 0, 0, 0, 4]
guessed_scores = [4, 1, 1, 0, 0, -2]
differences = compare(actual_scores, guessed_scores)
print(differences)  # Output: [4, 4, 1, 0, 0, 6]
```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Run the Code**: You can directly run the Python script or import the `compare` function into your own Python projects.

## How to Use

1. **Prepare Your Data**: Ensure you have two lists of equal length, one for actual scores and one for guessed scores.

2. **Call the Function**: Use the `compare` function to calculate the differences between the actual and guessed scores.

3. **Interpret the Results**: The output list will show how far off each guess was, with 0 indicating a correct guess.

This tool is designed to be simple and efficient, providing immediate feedback on the accuracy of score predictions. It can be easily integrated into larger projects or used as a standalone utility for quick evaluations.
```