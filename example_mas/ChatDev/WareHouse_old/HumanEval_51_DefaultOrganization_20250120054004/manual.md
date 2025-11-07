# Remove Vowels

A simple Python application to remove vowels from a given string.

## Introduction

The `remove_vowels` function is designed to take a string as input and return a new string with all vowels removed. This function is useful for text processing tasks where vowels need to be excluded from the text.

## Main Function

### `remove_vowels(text)`

- **Description**: This function takes a string and returns a new string with all vowels (both uppercase and lowercase) removed.
- **Parameters**: 
  - `text` (str): The input string from which vowels will be removed.
- **Returns**: 
  - `str`: A new string with all vowels removed.

#### Example Usage

```python
print(remove_vowels('abcdef'))  # Output: 'bcdf'
print(remove_vowels('aaBAA'))   # Output: 'B'
print(remove_vowels('zbcd'))    # Output: 'zbcd'
```

## Installation

### Environment Setup

This application does not require any external dependencies, making it simple to set up and run. You only need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can directly run the `main.py` file to test the function.
   ```bash
   python main.py
   ```

## Usage

To use the `remove_vowels` function, simply import it into your Python script and call it with the desired string. Here's a quick example:

```python
from main import remove_vowels

text = "Hello World"
result = remove_vowels(text)
print(result)  # Output: 'Hll Wrld'
```

## Conclusion

This simple utility function can be integrated into larger text processing pipelines where vowel removal is necessary. With no external dependencies, it is lightweight and easy to incorporate into any Python project.