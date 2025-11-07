# Count Uppercase Vowels in Even Indices

This software provides a simple function to count the number of uppercase vowels located at even indices in a given string. This can be useful for text analysis and processing tasks where specific character patterns need to be identified.

## Main Functionality

The main functionality of this software is encapsulated in the `count_upper` function. This function takes a single string as input and returns the count of uppercase vowels ('A', 'E', 'I', 'O', 'U') that appear at even indices within the string.

### Function: `count_upper(s)`

- **Input**: A string `s`.
- **Output**: An integer representing the number of uppercase vowels at even indices.

#### Example Usage

```python
count_upper('aBCdEf')  # Returns: 1
count_upper('abcdefg')  # Returns: 0
count_upper('dBBE')     # Returns: 0
```

## Installation

This software does not require any external dependencies beyond the standard Python library. Therefore, no additional installation steps are necessary.

### Requirements

- Python 3.x

## How to Use

1. **Ensure Python is Installed**: Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Run the Function**: You can use the `count_upper` function directly in your Python scripts. Simply import the function from the `main.py` file and call it with your desired string.

### Example Script

```python
from main import count_upper

# Test the function with different strings
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))     # Output: 0
```

## Conclusion

This software provides a straightforward utility for counting uppercase vowels at even indices in a string. It is easy to integrate into larger projects or use as a standalone tool for text processing tasks. With no external dependencies, it is simple to set up and use immediately.