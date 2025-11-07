# Same Characters Checker

This software provides a simple function to check if two words have the same characters, regardless of their order or frequency. This can be useful in various applications where character composition is more important than character sequence.

## Main Function

The main function provided by this software is `same_chars`, which takes two strings as input and returns a boolean indicating whether the two strings contain the same set of characters.

### Function Definition

```python
def same_chars(s0: str, s1: str) -> bool:
    return set(s0) == set(s1)
```

### Usage Examples

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

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file containing the function.

3. No additional installation steps are required since there are no external dependencies.

## How to Use

1. Open a Python environment (such as a Python shell, Jupyter notebook, or a Python script).

2. Import the `same_chars` function from the `main.py` file.

3. Call the `same_chars` function with two string arguments to check if they have the same characters.

Example:

```python
from main import same_chars

result = same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
print(result)  # Output: True
```

## Documentation

For further information or to report issues, please contact our support team. This software is designed to be simple and efficient, with no additional configuration required.