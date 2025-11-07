manual.md

```
# Compare Game Scores with Guesses

This software provides a simple utility to compare actual game scores with guessed scores and return the differences. It is designed to help users determine how accurate their guesses were in comparison to the actual results.

## Main Functionality

The main function of this software is to compare two lists: one containing the actual scores of games and the other containing the guessed scores. It returns a list of the same length, where each element represents the absolute difference between the guessed score and the actual score for that match. If the guess is correct, the difference is 0.

### Example Usage

- `compare([1,2,3,4,5,1],[1,2,3,4,2,-2])` returns `[0,0,0,0,3,3]`
- `compare([0,5,0,0,0,4],[4,1,1,0,0,-2])` returns `[4,4,1,0,0,6]`

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Script:**
   You can directly run the `main.py` script using Python:
   ```bash
   python main.py
   ```

## How to Use

1. **Prepare Your Data:**
   - Create two lists: one for the actual game scores and one for the guessed scores. Ensure both lists are of equal length.

2. **Call the Function:**
   - Use the `compare` function to get the differences between the actual scores and the guesses.
   - Example:
     ```python
     actual_scores = [1, 2, 3, 4, 5, 1]
     guessed_scores = [1, 2, 3, 4, 2, -2]
     differences = compare(actual_scores, guessed_scores)
     print(differences)  # Output: [0, 0, 0, 0, 3, 3]
     ```

3. **Interpret the Results:**
   - The output list will show `0` for each correctly guessed score and the absolute difference for incorrect guesses.

## Additional Information

This software is designed to be lightweight and easy to use, with no additional setup required beyond having Python installed. It is ideal for users who want a quick and efficient way to compare game scores with their guesses.

For any further questions or support, please contact our support team.
```