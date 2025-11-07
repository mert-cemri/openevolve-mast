manual.md

```
# same_chars Function

A simple Python function to check if two strings have the same set of characters.

## Overview

The `same_chars` function is designed to determine whether two given strings contain the same characters, regardless of their order or frequency. This can be useful in various applications where character composition is more important than the sequence or count of characters.

## Main Functionality

- **Function Name**: `same_chars`
- **Input**: Two strings (`s0` and `s1`)
- **Output**: Boolean (`True` or `False`)
  - Returns `True` if both strings have the same set of characters.
  - Returns `False` otherwise.

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

This function does not require any external dependencies, making it easy to integrate into any Python project.

### Requirements

- Python 3.x

### Installation Steps

1. **Clone the Repository**: If the function is part of a larger project, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your working directory to where the `main.py` file is located.
   ```bash
   cd <project-directory>
   ```

3. **Run the Function**: You can directly run the function in a Python environment or integrate it into your existing codebase.

## How to Use

1. **Import the Function**: If you are using this function in another script, make sure to import it.
   ```python
   from main import same_chars
   ```

2. **Call the Function**: Pass two strings as arguments to the function.
   ```python
   result = same_chars('string1', 'string2')
   print(result)  # Outputs: True or False
   ```

## Additional Information

- **No External Libraries**: This function is self-contained and does not rely on any third-party libraries, ensuring compatibility and ease of use.
- **Efficiency**: The function uses Python's set data structure, which provides an efficient way to compare character sets.

Feel free to modify and adapt the function to suit your specific needs. If you encounter any issues or have suggestions for improvements, please reach out to the development team.
```