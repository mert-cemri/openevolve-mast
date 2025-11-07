# Histogram Function User Manual

Welcome to the user manual for the Histogram Function. This software is designed to analyze a string of space-separated lowercase letters and return a dictionary of the letter(s) with the highest frequency, along with their corresponding count.

## Main Functionality

The main function provided by this software is the `histogram` function. It processes a string input and outputs a dictionary containing the letter(s) with the most repetitions and their counts. This function is useful for analyzing text data to determine the most frequently occurring letters.

### Example Usage

- `histogram('a b c')` returns `{'a': 1, 'b': 1, 'c': 1}`
- `histogram('a b b a')` returns `{'a': 2, 'b': 2}`
- `histogram('a b c a b')` returns `{'a': 2, 'b': 2}`
- `histogram('b b b b a')` returns `{'b': 4}`
- `histogram('')` returns `{}`

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `histogram` function.

3. **Run the code**: You can execute the code using any Python environment or directly from the command line.

## How to Use

1. **Prepare your input**: Ensure your input is a string of space-separated lowercase letters.

2. **Call the `histogram` function**: Pass your prepared string to the `histogram` function.

3. **Receive the output**: The function will return a dictionary with the letter(s) that have the highest frequency and their counts.

## Documentation

For further details on the implementation and usage of the `histogram` function, please refer to the comments within the `main.py` file. The code is well-documented to provide clarity on how the function operates.

## Support

If you encounter any issues or have questions regarding the usage of this software, please feel free to reach out to our support team. We are here to assist you in making the most out of the Histogram Function.

Thank you for choosing our software to analyze your text data!