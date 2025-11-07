# Split Words Software

This software provides a function to process a given string of words and return a list of words split based on specific criteria. It is designed to handle strings with whitespace, commas, or calculate a specific count based on lowercase letters.

## Main Functions

The main function of this software is `split_words(txt)`, which operates as follows:

- **Whitespace Split**: If the input string contains whitespace, the function splits the string into a list of words based on the whitespace.
- **Comma Split**: If the input string does not contain whitespace but contains commas, the function splits the string into a list of words based on the commas.
- **Odd Order Count**: If the input string contains neither whitespace nor commas, the function returns the count of lowercase letters in the string that have an odd order in the alphabet (where `ord('a') = 0`, `ord('b') = 1`, ..., `ord('z') = 25`).

### Examples

- `split_words("Hello world!")` returns `["Hello", "world!"]`
- `split_words("Hello,world!")` returns `["Hello", "world!"]`
- `split_words("abcdef")` returns `3`

## Installation

This software does not require any external dependencies, making it easy to set up and use. You simply need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone or download the repository containing the `main.py` file.

## Usage

To use the `split_words` function, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run the Python script by executing the command: `python main.py`.

This will execute the example usage of the `split_words` function and display the results in the terminal.

### Custom Usage

To use the function with your own input, you can modify the `main.py` file:

1. Open `main.py` in a text editor.
2. Replace the example usage at the bottom of the file with your own input, like so:
   ```python
   print(split_words("Your custom input here"))
   ```
3. Save the changes and run the script again using the command: `python main.py`.

This will display the output based on your custom input.

## Documentation

For further details on how the function works or to contribute to the project, please refer to the comments within the `main.py` file. The code is documented to provide clarity on the logic and functionality implemented.