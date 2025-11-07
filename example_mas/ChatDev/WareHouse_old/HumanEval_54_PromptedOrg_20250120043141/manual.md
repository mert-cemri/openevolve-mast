# same_chars Function User Manual

## Introduction

The `same_chars` function is a simple Python utility designed to check if two strings contain the same set of characters, regardless of their order or frequency. This can be useful in various applications where character set comparison is necessary.

## Main Function

### same_chars(s0: str, s1: str) -> bool

- **Description**: This function takes two strings as input and returns a boolean value indicating whether both strings contain the same characters.
- **Parameters**:
  - `s0` (str): The first string to compare.
  - `s1` (str): The second string to compare.
- **Returns**: 
  - `True` if both strings contain the same set of characters.
  - `False` otherwise.

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

The `same_chars` function does not require any external dependencies, making it straightforward to integrate into any Python environment. 

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Code**: Obtain the `main.py` file containing the `same_chars` function. You can clone the repository or download the file directly.

3. **Run the Code**: You can run the code directly in your Python environment. No additional setup is required.

### Running the Function

To use the `same_chars` function, simply import it into your Python script or interactive session and call it with the desired string inputs.

```python
from main import same_chars

result = same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
print(result)  # Output: True
```

## Conclusion

The `same_chars` function is a lightweight and efficient tool for comparing the character sets of two strings. With no external dependencies, it is easy to integrate and use in any Python project.