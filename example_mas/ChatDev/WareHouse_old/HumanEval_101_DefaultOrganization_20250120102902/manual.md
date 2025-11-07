manual.md

```
# Words String Splitter

A simple Python utility to split a string of words separated by commas or spaces into a list of words.

## Overview

The Words String Splitter is a straightforward Python function designed to take a string input and return a list of words. This function is particularly useful for parsing sentences or phrases where words are separated by commas or spaces.

## Main Function

### `words_string(s)`

- **Description**: Splits a string of words separated by commas or spaces into a list of words.
- **Parameters**: 
  - `s` (str): A string of words separated by commas or spaces.
- **Returns**: 
  - `list`: A list of words.
- **Examples**:
  - `words_string("Hi, my name is John")` returns `["Hi", "my", "name", "is", "John"]`
  - `words_string("One, two, three, four, five, six")` returns `["One", "two", "three", "four", "five", "six"]`

## Installation

### Environment Setup

This project does not require any external dependencies, making it easy to set up and run. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the code**: You can directly run the `main.py` file to test the function.
   ```bash
   python main.py
   ```

## Usage

To use the `words_string` function, simply import it into your Python script and call it with a string argument. Here's a quick example:

```python
from main import words_string

# Example usage
sentence = "Hello, world, this is a test"
words = words_string(sentence)
print(words)  # Output: ['Hello', 'world', 'this', 'is', 'a', 'test']
```

## Support

For any issues or questions, please contact our support team or visit our documentation page for more detailed information.

```