manual.md

```
# Vowel Counter

A simple Python application to count the number of vowels in a given string. This application is designed to handle both lowercase and uppercase letters and considers 'y' as a vowel only when it appears at the end of the word.

## Main Functions

### `vowels_count(s)`

- **Description**: This function takes a string `s` as input and returns the number of vowels in the string. The vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' (only when 'y' is at the end of the word).
- **Parameters**: 
  - `s` (str): The input string for which the vowels need to be counted.
- **Returns**: 
  - (int): The number of vowels in the input string.

### `test_vowels_count()`

- **Description**: This function contains a set of test cases to verify the correctness of the `vowels_count` function. It asserts various scenarios to ensure the function behaves as expected.
- **Usage**: Run this function to execute all the test cases and validate the functionality of the `vowels_count` function.

## Installation

This application does not require any external dependencies. It is built using standard Python libraries. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Navigate to the directory** containing the `main.py` file.

3. **Run the application** using Python:
   ```bash
   python main.py
   ```

## How to Use

1. **Open the `main.py` file** in a text editor or IDE of your choice.

2. **Modify the `vowels_count` function** if needed to customize the vowel counting logic.

3. **Run the `test_vowels_count` function** to ensure all test cases pass and the function works as expected.

4. **Use the `vowels_count` function** in your own applications by importing it from `main.py`.

## Example Usage

```python
from main import vowels_count

# Example usage
word = "university"
vowel_count = vowels_count(word)
print(f"The number of vowels in '{word}' is {vowel_count}.")
```

## Documentation

For further details on the implementation and test cases, please refer to the comments within the `main.py` file.

```