# Vowels Count Application

This application provides a function to count the number of vowels in a given string. The vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' (only when 'y' is at the end of the word). The application includes a set of test cases to ensure the function works correctly.

## Main Functionality

The main functionality of this application is the `vowels_count` function, which takes a string as input and returns the number of vowels in that string. The function is case-insensitive and considers 'y' as a vowel only when it appears at the end of the word.

### Example Usage

```python
# Example usage of the vowels_count function
result = vowels_count("abcde")
print(result)  # Output: 2

result = vowels_count("ACEDY")
print(result)  # Output: 3
```

## Installation

This application does not require any external dependencies, so no installation of additional packages is necessary. Ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Application**: Execute the `main.py` file to run the test cases and verify the functionality of the `vowels_count` function.

   ```bash
   python main.py
   ```

   You should see the output indicating that all test cases have passed:

   ```
   All test cases passed.
   ```

4. **Modify or Extend**: You can modify the `main.py` file to add more test cases or use the `vowels_count` function with different inputs as needed.

## Documentation

The code is documented with comments and docstrings to help you understand the functionality of each part. The `vowels_count` function is defined with a clear docstring explaining its purpose and usage.

Feel free to explore and modify the code to suit your needs. If you encounter any issues or have questions, please refer to the comments within the code for guidance.