# Vowel Counter

This software provides a simple utility to count the number of vowels in a given string. The vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' if it is at the end of the word. This tool is useful for linguistic analysis, educational purposes, or any application where vowel counting is required.

## Features

- **Vowel Counting**: Accurately counts vowels in a string, considering 'y' as a vowel only when it appears at the end of the word.
- **Comprehensive Test Cases**: Includes a variety of test cases to ensure the function works correctly across different scenarios.

## Installation

This software does not require any external dependencies beyond Python itself. It is compatible with Python version 3.6 and above.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone or download the repository containing the `main.py` file.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the script using Python:

   ```bash
   python main.py
   ```

This will execute the script and run the test cases to validate the functionality of the `vowels_count` function. If all test cases pass, you will see the message "All test cases passed!" in the terminal.

## Functionality

### `vowels_count(s)`

- **Description**: Counts the number of vowels in a given string. Vowels are 'a', 'e', 'i', 'o', 'u', and 'y' if it is at the end of the word.
- **Parameters**: 
  - `s` (str): The input string.
- **Returns**: 
  - `int`: The number of vowels in the string.

### Example Usage

```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

## Testing

The script includes a function `test_vowels_count()` that runs a series of test cases to ensure the `vowels_count` function behaves as expected. These test cases cover various scenarios, including:

- Strings with different combinations of vowels and consonants.
- Strings with uppercase and lowercase letters.
- Edge cases such as empty strings and strings without vowels.

To run the tests, simply execute the `main.py` script as described in the Usage section.