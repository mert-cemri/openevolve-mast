# same_chars Function User Manual

Welcome to the user manual for the `same_chars` function. This function is designed to check if two words have the same characters, regardless of the order or frequency of those characters.

## Main Functionality

The `same_chars` function takes two strings as input and returns a boolean value indicating whether the two strings contain the same set of characters. This function is useful for tasks where you need to verify if two words are composed of the same characters.

### Function Signature

```python
def same_chars(s0: str, s1: str) -> bool:
```

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

This function is implemented in Python and does not require any external dependencies. You can use it directly in your Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py`.

4. Run the Python script using your preferred Python interpreter.

## How to Use

1. Open the `main.py` file in your preferred code editor.

2. Use the `same_chars` function by passing two strings as arguments.

3. The function will return `True` if the two strings contain the same characters, and `False` otherwise.

### Example

```python
# Example usage
result = same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
print(result)  # Output: True
```

## Documentation

The `same_chars` function is straightforward and does not require additional documentation beyond the examples provided. It leverages Python's set data structure to compare the unique characters in each string.

For any further questions or support, please contact our support team. We hope this function meets your needs and enhances your development process.