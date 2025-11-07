manual.md

```
# Vowels Count Application

This application provides a simple utility function to count the number of vowels in a given string. It considers the vowels 'a', 'e', 'i', 'o', 'u' and treats 'y' as a vowel only when it appears at the end of the word.

## Main Functionality

The core functionality of this application is encapsulated in the `vowels_count` function. This function takes a string as input and returns the number of vowels present in that string according to the specified rules.

### Function Definition

```python
def vowels_count(s):
    """
    Takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.
    """
```

### Example Usage

```python
>>> vowels_count("abcde")
2
>>> vowels_count("ACEDY")
3
```

## Installation

This application does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory containing the `main.py` file:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Application**: Execute the `main.py` file to run the test cases and verify the functionality:

   ```bash
   python main.py
   ```

## Usage

The application includes a set of predefined test cases to validate the functionality of the `vowels_count` function. These test cases cover various scenarios, including:

- Words with standard vowels
- Words with 'y' as a vowel at the end
- Words with no vowels
- Edge cases such as empty strings

To run the test cases, simply execute the `main.py` file as shown in the installation section. The assertions will verify that the function behaves as expected.

## Documentation

For further information on how the function works or to extend its functionality, you can refer to the comments and docstrings within the `main.py` file. These provide detailed explanations of the logic and expected behavior of the function.

Feel free to modify the test cases or the function itself to suit your specific needs or to explore additional edge cases.
```

This manual provides a comprehensive guide to using the Vowels Count Application, including installation instructions, usage examples, and documentation references.