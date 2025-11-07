manual.md

```
# Compare Function

This software provides a simple Python function to compare two lists of scores and guesses. The function calculates the absolute difference between each pair of corresponding elements in the lists, helping users determine how accurate their guesses were compared to the actual scores.

## Main Function

The main function provided by this software is `compare(game, guess)`. It takes two lists as input:

- `game`: A list of integers representing the actual scores of the matches.
- `guess`: A list of integers representing the guessed scores of the matches.

The function returns a list of integers, where each element is the absolute difference between the corresponding elements of the `game` and `guess` lists. If a guess is correct, the difference is 0.

### Example Usage

```python
# Example 1
result = compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2])
print(result)  # Output: [0, 0, 0, 0, 3, 3]

# Example 2
result = compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2])
print(result)  # Output: [4, 4, 1, 0, 0, 6]
```

## Installation

This software does not require any external dependencies, making it easy to use in any Python environment. Simply ensure you have Python installed on your system.

### Quick Install

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

2. **Download the Code**: Save the `main.py` file containing the `compare` function to your local machine.

3. **Run the Code**: You can run the code using any Python interpreter. Open a terminal or command prompt, navigate to the directory containing `main.py`, and execute your Python script.

## How to Use

1. **Prepare Your Data**: Create two lists of integers, one for the actual scores and one for the guessed scores. Ensure both lists are of equal length.

2. **Call the Function**: Use the `compare` function by passing your lists as arguments.

3. **Interpret the Results**: The function will return a list of absolute differences. A value of 0 indicates a correct guess, while any other value indicates the magnitude of the error.

This simple yet effective function can be used in various applications where score predictions and evaluations are necessary.
```