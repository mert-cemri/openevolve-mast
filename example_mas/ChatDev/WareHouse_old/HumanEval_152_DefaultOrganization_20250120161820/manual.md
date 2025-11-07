manual.md

```
# Score Comparison Software

This software is designed to compare two lists of scores and guesses, determining how accurately the guesses match the actual scores. It provides a simple and efficient way to evaluate the accuracy of predictions in various scenarios, such as sports matches or other competitive events.

## Main Functionality

The core functionality of this software is encapsulated in the `compare` function. This function takes two lists as input: one representing the actual scores of a series of matches, and the other representing the guessed scores. It returns a list of integers indicating the difference between each guessed score and the actual score. If a guess is correct, the difference is 0; otherwise, it is the absolute difference between the guessed and actual scores.

### Function Signature

```python
def compare(game, guess):
    """
    Parameters:
    game (list of int): The actual scores of the matches.
    guess (list of int): The guessed scores of the matches.
    
    Returns:
    list of int: A list of differences between the actual scores and the guessed scores.
    """
```

### Examples

- `compare([1,2,3,4,5,1],[1,2,3,4,2,-2])` returns `[0,0,0,0,3,3]`
- `compare([0,5,0,0,0,4],[4,1,1,0,0,-2])` returns `[4,4,1,0,0,6]`

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the repository is cloned:
   ```bash
   cd <repository-directory>
   ```

3. **Run the Software**: Execute the `main.py` file to use the `compare` function:
   ```bash
   python main.py
   ```

## Usage

To use the `compare` function, simply call it with two lists of integers representing the actual scores and the guessed scores. The function will return a list of differences, which you can use to analyze the accuracy of the guesses.

### Example Usage

```python
# Example usage of the compare function
actual_scores = [1, 2, 3, 4, 5, 1]
guessed_scores = [1, 2, 3, 4, 2, -2]
differences = compare(actual_scores, guessed_scores)
print(differences)  # Output: [0, 0, 0, 0, 3, 3]
```

## Documentation

For further information and detailed documentation, please refer to the comments within the `main.py` file. The function is well-documented to assist in understanding its usage and functionality.

```