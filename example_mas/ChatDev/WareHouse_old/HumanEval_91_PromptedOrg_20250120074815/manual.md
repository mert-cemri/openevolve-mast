# Boredom Counter

This software provides a function `is_bored` that counts the number of sentences starting with the word "I" in a given string. Sentences are delimited by '.', '?' or '!'. This can be useful for analyzing text to determine how often sentences begin with a specific pronoun, which might indicate a certain style or focus in writing.

## Main Function

### `is_bored(S)`

- **Description**: This function takes a string `S` and returns the number of sentences that start with the word "I".
- **Parameters**: 
  - `S` (str): A string containing sentences.
- **Returns**: 
  - `int`: The count of sentences starting with "I".

#### Example Usage

```python
>>> is_bored("Hello world")
0
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
```

## Installation

This software does not require any external dependencies beyond the standard Python library. However, to ensure you have Python installed, follow these steps:

1. **Install Python**: 
   - Download and install the latest version of Python from [python.org](https://www.python.org/downloads/).
   - Ensure that Python is added to your system's PATH during installation.

2. **Verify Installation**:
   - Open a terminal or command prompt.
   - Run the command `python --version` to verify that Python is installed correctly.

## How to Use

1. **Create a Python Script**:
   - Create a new Python file, e.g., `main.py`.
   - Copy the `is_bored` function code into this file.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing your `main.py` file.
   - Run the script using the command `python main.py`.

3. **Test the Function**:
   - You can test the function by calling it with different strings and printing the results.
   - Example:
     ```python
     print(is_bored("I am happy. You are here. I enjoy coding!"))
     ```

This will output `2`, as there are two sentences starting with "I".

## Documentation

For further information on Python and its capabilities, please refer to the [official Python documentation](https://docs.python.org/3/).

This manual provides a basic overview of how to use the `is_bored` function. For more complex text analysis, consider integrating this function into larger applications or scripts.