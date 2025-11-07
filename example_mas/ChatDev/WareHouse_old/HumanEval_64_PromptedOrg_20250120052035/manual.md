# Vowels Count Application

This application provides a function to count the number of vowels in a given string. The vowels considered are 'a', 'e', 'i', 'o', 'u', and 'y' (only when 'y' is at the end of the word).

## Main Functionality

The main function of this application is `vowels_count`, which takes a string as input and returns the number of vowels in that string. It also includes a set of test cases to verify the correctness of the function.

### Function: `vowels_count`

- **Description**: Counts the number of vowels in a string. Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only when it is at the end of the word.
- **Input**: A string `s`.
- **Output**: An integer representing the number of vowels in the string.

### Example Usage

```python
>>> vowels_count("abcde")
2
>>> vowels_count("ACEDY")
3
```

## Installation

To use this application, you need to have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/).

## Running the Application

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to the cloned repository:
   ```bash
   cd <repository-directory>
   ```

3. **Run the Application**: Execute the Python script to run the test cases and verify the function:
   ```bash
   python main.py
   ```

## Test Cases

The application includes a set of test cases to ensure the `vowels_count` function works as expected. The test cases cover various scenarios, including:

- Strings with different combinations of vowels.
- Strings with 'y' at the end.
- Strings with no vowels.
- Upper and lower case letters.

### Example Test Cases

```python
assert vowels_count("hello") == 2
assert vowels_count("sky") == 1
assert vowels_count("rhythm") == 0
assert vowels_count("AEIOUY") == 6
assert vowels_count("bcd") == 0
```

Running the script will automatically execute these test cases and print "All test cases passed." if they are successful.

## Conclusion

This application provides a simple yet effective way to count vowels in a string, with comprehensive test cases to ensure accuracy. It is easy to set up and run, making it a useful tool for developers working with text processing in Python.