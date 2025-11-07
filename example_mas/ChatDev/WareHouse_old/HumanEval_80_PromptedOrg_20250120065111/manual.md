# Happy String Checker

This software provides a function to determine if a given string is "happy." A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.

## Main Functionality

The main function provided by this software is `is_happy(s)`. This function checks whether a given string `s` is happy according to the defined criteria.

### Function Definition

```python
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    """
```

### Examples

- `is_happy("a")` => `False`
- `is_happy("aa")` => `False`
- `is_happy("abcd")` => `True`
- `is_happy("aabb")` => `False`
- `is_happy("adb")` => `True`
- `is_happy("xyy")` => `False`

## Installation

This software is written in Python and does not require any external dependencies. Ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: 
   ```bash
   cd <repository-directory>
   ```

4. **Run the Code**: You can run the code using Python:
   ```bash
   python main.py
   ```

## Usage

To use the `is_happy` function, simply call it with a string argument. The function will return `True` if the string is happy and `False` otherwise.

### Example Usage

```python
# Example usage of the is_happy function
print(is_happy("abcd"))  # Output: True
print(is_happy("aabb"))  # Output: False
```

## Documentation

For more detailed documentation, refer to the comments within the code. The function is straightforward and does not require additional libraries or frameworks.

## Support

For any issues or questions, please contact the development team at support@chatdev.com. We are here to assist you with any inquiries or troubleshooting needs.