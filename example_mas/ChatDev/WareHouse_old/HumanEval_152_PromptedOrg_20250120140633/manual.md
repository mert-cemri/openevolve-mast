manual.md

```
# Compare Function

The Compare Function is a simple Python utility designed to evaluate the accuracy of guesses against actual scores in a series of matches. It calculates the absolute difference between each guess and the actual score, providing a clear measure of how accurate each guess was.

## Main Functionality

The primary function of this software is:

- **compare(game, guess):** This function takes two lists of integers, `game` and `guess`, both of equal length. Each index in these lists represents a match. The function returns a list of integers where each element is the absolute difference between the corresponding elements in `game` and `guess`. If a guess is correct, the difference is 0.

### Example Usage

```python
# Example 1
result = compare([1,2,3,4,5,1], [1,2,3,4,2,-2])
print(result)  # Output: [0,0,0,0,3,3]

# Example 2
result = compare([0,5,0,0,0,4], [4,1,1,0,0,-2])
print(result)  # Output: [4,4,1,0,0,6]
```

## Installation

This software does not require any external dependencies, making it straightforward to use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository:**
   - You can clone the repository using Git or download the ZIP file and extract it to your desired location.

3. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

4. **Run the Script:**
   - You can run the script using Python by executing the following command:
     ```bash
     python main.py
     ```

## Usage

To use the `compare` function, you can either import it into another Python script or run it directly in an interactive Python session. Here's how you can use it in a script:

```python
from main import compare

# Define your game scores and guesses
game_scores = [1, 2, 3, 4, 5, 1]
guesses = [1, 2, 3, 4, 2, -2]

# Get the result
result = compare(game_scores, guesses)

# Print the result
print(result)  # Output: [0, 0, 0, 0, 3, 3]
```

## Conclusion

The Compare Function is a straightforward tool for evaluating the accuracy of guesses against actual scores. With no external dependencies required, it is easy to set up and use in any Python environment.
```