manual.md

```
# Same Characters Checker

A simple Python module to check if two strings have the same set of characters.

## Overview

The `same_chars` function is designed to determine if two input strings contain the same characters, regardless of their order or frequency. This can be useful in various applications where character composition is more important than sequence or repetition.

## Main Function

### `same_chars(s0: str, s1: str) -> bool`

- **Description**: This function checks if two words have the same set of characters.
- **Parameters**:
  - `s0`: The first string to compare.
  - `s1`: The second string to compare.
- **Returns**: `True` if both strings have the same characters, `False` otherwise.

### Example Usage

```python
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
True
>>> same_chars('abcd', 'dddddddabc')
True
>>> same_chars('dddddddabc', 'abcd')
True
>>> same_chars('eabcd', 'dddddddabc')
False
>>> same_chars('abcd', 'dddddddabce')
False
>>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
False
```

## Installation

### Environment Setup

This module does not require any external dependencies, making it easy to integrate into existing Python projects.

1. **Ensure Python is installed**: This module requires Python to run. You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or Download the Repository**: You can clone the repository using Git or download the ZIP file and extract it.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your current directory to the project directory.

   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can directly run the `main.py` file to test the function.

   ```bash
   python main.py
   ```

## Usage

To use the `same_chars` function in your own projects, simply import the function from the module and call it with your desired strings.

```python
from main import same_chars

result = same_chars('string1', 'string2')
print(result)  # Outputs: True or False
```

## Conclusion

The Same Characters Checker is a straightforward and efficient tool for comparing the character sets of two strings. Its simplicity and lack of external dependencies make it a versatile addition to any Python project.
```
