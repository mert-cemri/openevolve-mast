# Distinct Character Counter

This software module provides a simple function to count the number of distinct characters in a given string, regardless of case sensitivity. It is implemented in Python and is designed to be straightforward and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this software is encapsulated in the `count_distinct_characters` function. This function takes a single string as input and returns an integer representing the number of distinct characters in the string, ignoring case differences.

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

1. **Case Insensitivity**: The function converts the input string to lowercase to ensure that character comparisons are case-insensitive.
2. **Distinct Characters**: It uses a set to automatically filter out duplicate characters, as sets inherently store only unique items.
3. **Count**: The function returns the length of this set, which corresponds to the number of distinct characters.

## Installation

### Prerequisites

- **Python**: Ensure you have Python installed on your system. This module is compatible with Python 3.x.

### Installation Steps

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the Directory**: Change into the directory containing the `main.py` file.
   ```bash
   cd <directory-name>
   ```

3. **No External Dependencies**: This project does not require any external Python packages, so no additional installation steps are necessary.

## Usage

To use the `count_distinct_characters` function, follow these steps:

1. **Open a Python Environment**: You can use a Python shell, script, or an integrated development environment (IDE) like PyCharm or VSCode.

2. **Import the Function**: Ensure that the `main.py` file is in your working directory or adjust your Python path accordingly.

3. **Call the Function**: Use the function with your desired input string.

### Example

```python
from main import count_distinct_characters

# Example usage
result1 = count_distinct_characters('xyzXYZ')
print(result1)  # Output: 3

result2 = count_distinct_characters('Jerry')
print(result2)  # Output: 4
```

## Conclusion

This module provides a simple yet effective way to count distinct characters in a string, making it useful for text analysis and data processing tasks where character diversity is of interest. With no dependencies, it is easy to integrate into existing Python projects.