manual.md

```
# Boredom Counter

A simple Python application to count the number of "boredoms" in a given string of text. A "boredom" is defined as a sentence that starts with the word "I". Sentences are delimited by '.', '?' or '!'.

## Main Functionality

The main function provided by this application is `is_bored(S)`, which takes a string `S` as input and returns the count of sentences that start with the word "I".

### Example Usage

```python
from main import is_bored

# Example 1
result1 = is_bored("Hello world")
print(result1)  # Output: 0

# Example 2
result2 = is_bored("The sky is blue. The sun is shining. I love this weather")
print(result2)  # Output: 1
```

## Installation

This application does not require any external dependencies beyond Python itself. To use the application, ensure you have Python installed on your system.

### Steps to Install Python

1. **Download Python**: Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**: Follow the installation instructions provided on the website for your specific operating system.

3. **Verify Installation**: Open a terminal or command prompt and type `python --version` to verify that Python is installed correctly.

## How to Use

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine using the following command:
   ```
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located:
   ```
   cd <directory-name>
   ```

3. **Run the Script**: You can run the script directly using Python. For example:
   ```
   python main.py
   ```

4. **Use the Function in Your Code**: Import the `is_bored` function into your own Python scripts and use it as demonstrated in the example usage section.

## Additional Information

- **No External Libraries Required**: The application is designed to work with the standard Python library, so no additional installations are necessary.

- **Customization**: You can modify the `main.py` file to suit your specific needs, such as changing the delimiters or the word that defines a "boredom".

- **Support**: For any issues or questions, please contact the development team or refer to the documentation provided in the code comments.

```