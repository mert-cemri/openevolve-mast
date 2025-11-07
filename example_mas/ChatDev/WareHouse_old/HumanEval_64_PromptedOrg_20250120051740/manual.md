# Vowels Count Software

This software provides a function to count the number of vowels in a given string. The vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' (only when 'y' appears at the end of the word).

## Main Functions

### `vowels_count(s)`

- **Description**: This function takes a string `s` as input and returns the number of vowels in the string. The vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' (only if 'y' is at the end of the word).
- **Arguments**: 
  - `s` (str): The input string.
- **Returns**: 
  - `int`: The number of vowels in the string.

### `test_vowels_count()`

- **Description**: This function contains test cases to verify the correctness of the `vowels_count` function. It asserts various scenarios to ensure the function behaves as expected.

## Installation

This project does not require any external dependencies. You can run the software using Python without any additional installations.

### Quick Install

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

## Usage

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine. Alternatively, you can copy the code provided above into a file named `main.py`.

2. **Run the Software**: Open a terminal or command prompt and navigate to the directory containing `main.py`. Execute the following command to run the test cases and verify the functionality:

   ```bash
   python main.py
   ```

   If all test cases pass, you will see the message "All test cases passed."

3. **Using the `vowels_count` Function**: You can use the `vowels_count` function in your own scripts by importing it from `main.py`. Here's an example of how to use it:

   ```python
   from main import vowels_count

   word = "example"
   count = vowels_count(word)
   print(f"The number of vowels in '{word}' is {count}.")
   ```

## Documentation

For further information on how the function works, refer to the docstring provided in the `vowels_count` function within `main.py`. The docstring includes examples and detailed explanations of the function's behavior.

Feel free to modify and extend the test cases in `test_vowels_count` to suit your specific needs.