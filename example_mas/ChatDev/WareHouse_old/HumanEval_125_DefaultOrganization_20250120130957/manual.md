manual.md

```
# Split Words Application

This application provides a simple utility function to process a given string of words. The function `split_words` is designed to split the input text based on specific criteria and return the result accordingly.

## Main Functionality

The `split_words` function processes a string input in the following ways:

1. **Whitespace Splitting**: If the input string contains whitespace characters, the function splits the string into a list of words based on these spaces.

2. **Comma Splitting**: If the input string does not contain any whitespace but contains commas, the function splits the string into a list of words based on these commas.

3. **Odd Order Count**: If the input string contains neither whitespace nor commas, the function calculates the number of lowercase letters in the string that have an odd order in the alphabet (e.g., 'b', 'd', 'f', etc.) and returns this count.

## Installation

This project does not require any external dependencies. It is implemented in Python and can be run in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

To use the `split_words` function, follow these steps:

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Script**: Execute the script using Python. You can test the function with different inputs by modifying the example usage section in the `main.py` file.

   ```bash
   python main.py
   ```

4. **Example Usage**: The script includes example calls to the `split_words` function, demonstrating its behavior with different inputs:

   ```python
   print(split_words("Hello world!"))  # ➞ ["Hello", "world!"]
   print(split_words("Hello,world!"))  # ➞ ["Hello", "world!"]
   print(split_words("abcdef"))        # ➞ 3
   ```

## Documentation

For further details on the implementation and usage of the `split_words` function, please refer to the comments within the `main.py` file. The code is self-explanatory and includes examples to guide you through its functionality.

Feel free to modify the code to suit your specific needs or to integrate it into larger projects.
```
