# Vowels Count Software

This software provides a function to count the number of vowels in a given string. The vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' (only when 'y' is at the end of the word).

## Main Functions

### `vowels_count(s)`

- **Description**: This function takes a string as input and returns the number of vowels in the string. The vowels are 'a', 'e', 'i', 'o', 'u', and 'y' (only if it appears at the end of the word).
- **Arguments**: 
  - `s` (str): The input string.
- **Returns**: 
  - `int`: The number of vowels in the string.

### `test_vowels_count()`

- **Description**: This function contains test cases to verify the correctness of the `vowels_count` function. It asserts various scenarios to ensure the function behaves as expected.

## Installation

This software does not require any external dependencies. You can run it using Python 3.x. Ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Test Cases**: Execute the `main.py` file to run the test cases and verify the functionality of the `vowels_count` function.

   ```bash
   python main.py
   ```

   If all test cases pass, you will see the message "All test cases passed."

4. **Use the Function**: You can modify the `main.py` file to use the `vowels_count` function with your own input strings.

## Example Usage

```python
# Example usage of the vowels_count function
print(vowels_count("hello"))  # Output: 2
print(vowels_count("sky"))    # Output: 1
print(vowels_count("rhythm")) # Output: 0
```

## Documentation

For further details on the implementation and test cases, refer to the comments within the `main.py` file. The code is self-explanatory and includes examples of how the function works with different inputs.