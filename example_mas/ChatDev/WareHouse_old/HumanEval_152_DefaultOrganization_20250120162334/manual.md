manual.md

```
# Compare Function

This software provides a simple Python function to compare two lists of scores and guesses, returning a list of the absolute differences between them. This can be useful for determining how accurate a set of guesses were compared to the actual results.

## Main Functionality

The main functionality of this software is encapsulated in the `compare` function. This function takes two lists as input: one representing the actual scores of a series of matches, and the other representing the guessed scores. It returns a list where each element is the absolute difference between the corresponding elements of the input lists. If a guess is correct, the difference is 0.

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

This software does not require any external dependencies, making it straightforward to use. You simply need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change into the directory containing the `main.py` file:
   ```
   cd <directory-name>
   ```

4. **Run the Code**: You can run the code directly using Python:
   ```
   python main.py
   ```

## How to Use

To use the `compare` function, you need to import it from the `main.py` file and call it with your lists of actual scores and guesses. The function will return a list of the absolute differences.

### Example

```python
from main import compare

# Define your actual scores and guesses
actual_scores = [1, 2, 3, 4, 5, 1]
guessed_scores = [1, 2, 3, 4, 2, -2]

# Get the comparison result
differences = compare(actual_scores, guessed_scores)

# Output the result
print(differences)  # Output: [0, 0, 0, 0, 3, 3]
```

## Conclusion

This software provides a simple yet effective way to compare two lists of scores and guesses. With no external dependencies, it is easy to set up and use in any Python environment. Whether you're analyzing sports scores, exam results, or any other type of data, this function can help you quickly determine the accuracy of your guesses.
```