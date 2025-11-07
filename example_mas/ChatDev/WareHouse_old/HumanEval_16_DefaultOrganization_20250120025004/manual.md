manual.md

```
# Distinct Character Counter

This software provides a simple function to count the number of distinct characters in a given string, ignoring case sensitivity. It is designed to be straightforward and efficient, making it easy to integrate into larger applications or use as a standalone utility.

## Main Functionality

The core functionality of this software is encapsulated in the `count_distinct_characters` function. This function takes a string as input and returns the number of distinct characters, treating uppercase and lowercase versions of a character as the same.

### Function Definition

```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
```

### How It Works

1. **Case Insensitivity**: The function converts the input string to lowercase to ensure that character comparison is case insensitive.
2. **Distinct Characters**: It uses a set to store characters, as sets automatically handle duplicates and only store unique items.
3. **Count**: Finally, it returns the size of the set, which represents the number of distinct characters.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Move into the directory containing the `main.py` file.
   ```bash
   cd <directory-name>
   ```

3. **Run the Script**: You can run the script directly using Python.
   ```bash
   python main.py
   ```

## Usage

To use the `count_distinct_characters` function, simply import it into your Python script and call it with the desired string.

### Example Usage

```python
from main import count_distinct_characters

# Example strings
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

## Documentation

For further details on how to use this function or integrate it into larger projects, please refer to the inline documentation within the code or contact the development team for support.

```