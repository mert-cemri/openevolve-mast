# Compare Function User Manual

## Introduction

The `compare` function is a simple Python utility designed to compare two lists of scores and guesses. It calculates the difference between each pair of corresponding elements in the lists and returns a new list with these differences. This function is particularly useful for determining how accurate a set of guesses is compared to actual results.

## Main Functionality

- **Function Name**: `compare`
- **Purpose**: To determine the accuracy of guessed scores against actual scores.
- **Input**: Two lists of integers, `game` and `guess`, which must be of equal length.
- **Output**: A list of integers representing the absolute differences between the corresponding elements of the input lists. A value of `0` indicates a correct guess.

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

This project does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the code by cloning the repository or downloading the files directly.

3. **Run the Code**: Use any Python environment to run the `main.py` file containing the `compare` function.

## How to Use

1. **Prepare Your Data**: Ensure you have two lists of integers, `game` and `guess`, of equal length. These lists represent the actual scores and the guessed scores, respectively.

2. **Call the Function**: Use the `compare` function by passing your `game` and `guess` lists as arguments.

3. **Interpret the Results**: The function will return a list of differences. A `0` indicates a correct guess, while any other number represents the absolute difference between the guessed and actual scores.

## Conclusion

The `compare` function is a straightforward tool for evaluating the accuracy of guesses against actual results. With no external dependencies, it is easy to integrate into any Python project. Simply ensure your input lists are of equal length, and let the function handle the rest.