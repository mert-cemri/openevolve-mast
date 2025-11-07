manual.md

```
# Vowels Count Application

This application provides a simple utility function to count the number of vowels in a given string. The function `vowels_count` is designed to identify vowels in both uppercase and lowercase, and it also considers 'y' as a vowel when it appears at the end of the word.

## Main Functions

### `vowels_count(s)`

- **Description**: This function takes a string `s` as input and returns the number of vowels in the string. The vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' (only when 'y' is at the end of the word).

- **Parameters**: 
  - `s` (str): The input string representing a word.

- **Returns**: 
  - `int`: The number of vowels in the input string.

- **Example Usage**:
  ```python
  print(vowels_count("abcde"))  # Output: 2
  print(vowels_count("ACEDY"))  # Output: 3
  ```

## Installation

This application is written in Python and does not require any external dependencies. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Script**: Execute the script using Python to run the test cases and verify the functionality of the `vowels_count` function.
   ```bash
   python main.py
   ```

4. **Modify and Test**: You can modify the `vowels_count` function or add more test cases in the `test_vowels_count` function to suit your needs.

## Testing

The script includes a set of test cases to verify the correctness of the `vowels_count` function. These tests cover various scenarios, including different combinations of vowels and the special case where 'y' is considered a vowel.

To run the tests, simply execute the `main.py` file as shown above. The script will automatically run the test cases and assert the expected results.

## Contribution

Feel free to contribute to this project by adding more test cases or improving the function. Fork the repository, make your changes, and submit a pull request for review.

## Support

For any issues or questions, please contact the development team at ChatDev.

```