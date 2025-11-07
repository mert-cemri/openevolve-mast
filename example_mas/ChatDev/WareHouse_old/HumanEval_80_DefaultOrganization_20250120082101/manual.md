manual.md

```
# Happy String Checker

This software provides a simple function to determine if a given string is "happy". A string is considered "happy" if its length is at least 3 and every 3 consecutive letters are distinct.

## Main Functionality

The main function provided by this software is `is_happy(s)`, which checks if a string `s` is happy according to the defined criteria.

### Function Definition

```python
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    """
```

### Example Usage

- `is_happy("a")` returns `False`
- `is_happy("aa")` returns `False`
- `is_happy("abcd")` returns `True`
- `is_happy("aabb")` returns `False`
- `is_happy("adb")` returns `True`
- `is_happy("xyy")` returns `False`

## Installation

This software does not have any external dependencies, so no additional installation steps are required beyond having Python installed on your system.

### Prerequisites

- Python 3.x

### Installation Steps

1. Ensure you have Python installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py`.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python interpreter and import the `is_happy` function:

   ```bash
   python
   ```

   ```python
   from main import is_happy
   ```

4. Use the `is_happy` function by passing a string as an argument:

   ```python
   print(is_happy("abcd"))  # Output: True
   ```

5. Exit the Python interpreter by typing `exit()`.

## Additional Information

This software is designed to be lightweight and efficient, focusing solely on the task of determining if a string is "happy". It is suitable for educational purposes, quick checks, or integration into larger projects where such functionality is needed.

For any questions or support, please contact the development team at ChatDev.
```