manual.md

```
# Compare Function

This software provides a simple function to compare two lists of scores and guesses. It calculates the absolute difference between the corresponding elements of the two lists, indicating how far off each guess was from the actual score. If the guess is correct, the difference is 0.

## Main Functionality

The primary function of this software is:

- **compare(game, guess):** This function takes two lists of equal length as input: `game` (actual scores) and `guess` (guessed scores). It returns a list of the same length, where each element represents the absolute difference between the corresponding elements of the `game` and `guess` lists. If the guess matches the actual score, the difference is 0.

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

To use this software, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python:** Make sure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Set Up Virtual Environment (Optional):** It's a good practice to use a virtual environment to manage dependencies. You can create and activate a virtual environment using the following commands:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install Dependencies:** There are no additional dependencies required for this software. However, if you plan to extend the functionality, you can manage dependencies using a `requirements.txt` file.

## How to Use

1. **Clone the Repository:** Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:** Change into the directory where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Script:** You can run the script using Python to see the function in action.

   ```bash
   python main.py
   ```

4. **Modify and Extend:** Feel free to modify the `main.py` file to test different inputs or extend the functionality as needed.

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is straightforward and designed to be easily understandable and modifiable.

```