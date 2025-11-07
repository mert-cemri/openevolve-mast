manual.md

```
# Compare Function

The Compare Function is a simple Python utility designed to evaluate the accuracy of guessed scores against actual scores for a series of matches. This function is useful for scenarios where you need to determine how close a set of predictions or guesses are to the actual outcomes.

## Main Functionality

The primary function provided by this software is:

- `compare(game, guess)`: This function takes two lists of integers as input, `game` and `guess`, both of which should be of equal length. Each index in these lists represents a match. The function returns a list of integers where each element represents the absolute difference between the guessed score and the actual score. If the guess is correct, the difference is 0.

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

This project does not require any external dependencies, making it straightforward to use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: 
   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can directly run the `main.py` file to test the function:
   ```bash
   python main.py
   ```

## Usage

To use the `compare` function in your own projects:

1. **Import the Function**: Copy the function from `main.py` into your own Python script or module.

2. **Call the Function**: Use the function by passing two lists of equal length representing the actual scores and guessed scores.

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is well-documented to help you understand its usage and expected input/output.

```