# same_chars Function User Manual

## Introduction

The `same_chars` function is a simple Python utility designed to check if two strings contain the same set of characters, regardless of their order or frequency. This can be useful in various applications where character composition is more important than character sequence or repetition.

## Main Function

### `same_chars(s0: str, s1: str) -> bool`

- **Description**: This function takes two strings as input and returns `True` if both strings contain the exact same set of characters, and `False` otherwise.
- **Parameters**:
  - `s0` (str): The first string to compare.
  - `s1` (str): The second string to compare.
- **Returns**: `bool` - `True` if both strings have the same characters, `False` otherwise.

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

This function does not require any external dependencies, making it straightforward to integrate into any Python environment. Ensure you have Python installed on your system.

### Installation Steps

1. **Clone the Repository**: If the function is part of a larger codebase, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your working directory to where the `main.py` file is located.
   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can directly run the function in a Python environment or script.
   ```bash
   python main.py
   ```

## Usage

To use the `same_chars` function, simply import it into your Python script or interactive session and call it with the desired string inputs.

### Example

```python
from main import same_chars

result = same_chars('hello', 'olleh')
print(result)  # Output: True

result = same_chars('hello', 'world')
print(result)  # Output: False
```

## Conclusion

The `same_chars` function is a lightweight and efficient tool for comparing character sets between two strings. With no external dependencies, it is easy to integrate and use in various Python projects.