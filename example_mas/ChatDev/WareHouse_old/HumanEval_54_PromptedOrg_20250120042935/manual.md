# Same Characters Checker

This software provides a simple function to check if two words have the same characters. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function of this software is `same_chars(s0: str, s1: str) -> bool`. This function takes two strings as input and returns a boolean value indicating whether the two strings contain the same characters, regardless of their order or frequency.

### Function Signature

```python
def same_chars(s0: str, s1: str) -> bool:
```

### Parameters

- `s0`: The first string to compare.
- `s1`: The second string to compare.

### Returns

- `True` if both strings have the same characters.
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

This software does not require any external dependencies, so no installation of additional packages is necessary. You only need Python installed on your system.

## How to Use

1. **Clone the Repository**: Clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the function by importing it into your Python script or by running it directly in a Python shell.

### Example

```bash
python
```

```python
from main import same_chars

print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # Output: True
print(same_chars('abcd', 'dddddddabc'))  # Output: True
```

## Conclusion

This software provides a straightforward solution to check if two words have the same characters. It is easy to use and does not require any additional setup beyond having Python installed.