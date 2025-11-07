```markdown
# Palindrome Detection Application

This application is designed to detect palindromes in a given text file. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

## Main Functions

The application consists of three main components:

1. **FileHandler Module**: Handles file operations, specifically reading the content of a text file.
2. **PalindromeDetector Module**: Contains the logic to detect palindromes within the text.
3. **Main Module**: Executes the program by reading a text file, detecting palindromes, and printing them.

## Installation

### Environment Setup

To run this application, you need to have Python installed on your system. The application is compatible with Python version 3.6 and above.

### Install Dependencies

To install the necessary dependencies, you can use the following command:

```bash
pip install -r requirements.txt
```

This command will ensure that your environment is set up with the correct Python version.

## How to Use

1. **Prepare Your Text File**: Ensure you have a text file named `input.txt` in the same directory as the application. This file should contain the text you want to analyze for palindromes.

2. **Run the Application**: Execute the main module to start the palindrome detection process. Use the following command in your terminal:

```bash
python main.py
```

3. **View Results**: Once the program runs, it will output the detected palindromes from the text file to the console.

## Example

Suppose your `input.txt` contains the following text:

```
A man, a plan, a canal, Panama!
Was it a car or a cat I saw?
No lemon, no melon.
```

After running the application, the output will be:

```
Detected Palindromes:
A man, a plan, a canal, Panama
Was it a car or a cat I saw
No lemon, no melon
```

## Troubleshooting

- **File Not Found Error**: If you encounter an error stating that the file `input.txt` was not found, ensure that the file exists in the correct directory and that the file name is spelled correctly.

- **Python Version Error**: If you encounter issues related to the Python version, ensure that you have Python 3.6 or higher installed. You can check your Python version by running `python --version` in your terminal.

## Support

For further assistance, please contact our support team or visit our documentation page for more detailed guides and troubleshooting tips.

```
