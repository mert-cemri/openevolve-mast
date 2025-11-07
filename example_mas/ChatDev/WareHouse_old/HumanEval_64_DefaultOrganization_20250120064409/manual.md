# Vowel Counter

This software provides a simple utility to count the number of vowels in a given string. It considers 'a', 'e', 'i', 'o', 'u' as vowels, and 'y' as a vowel only when it appears at the end of the word.

## Main Functions

- **vowels_count(s)**: This function takes a string `s` as input and returns the number of vowels in the string. It is case-insensitive and treats 'y' as a vowel only if it is the last character in the string.

## Installation

This software does not require any external dependencies. It is implemented in Python and can be run in any standard Python environment.

### Prerequisites

- Python 3.x

### Installation Steps

1. Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing the `main.py` file.

## Usage

To use the vowel counting functionality, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the script using Python:

   ```bash
   python main.py
   ```

4. The script will execute the `test_vowels_count` function, which runs a series of test cases to verify the correctness of the `vowels_count` function. If all test cases pass, you will see the message "All test cases passed."

## Example

Here is an example of how the `vowels_count` function works:

```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

These examples demonstrate the function's ability to count vowels accurately, considering the special rule for 'y'.

## Documentation

For further details on the implementation and additional examples, please refer to the comments within the `main.py` file. The code is self-explanatory and includes inline comments to guide understanding.

Feel free to modify the code to suit your specific needs or to add more test cases to ensure robustness in different scenarios.