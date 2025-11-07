manual.md

```
# Overlapping Substring Counter

This software provides a simple function to count the number of times a given substring appears in a string, including overlapping occurrences. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The core functionality of this software is provided by the `how_many_times` function. This function takes two arguments:
- `string`: The original string in which to search for the substring.
- `substring`: The substring to search for within the original string.

The function returns an integer representing the number of times the substring is found in the string, including overlapping occurrences.

### Example Usage

```python
from main import how_many_times

# Example 1
result1 = how_many_times('', 'a')
print(result1)  # Output: 0

# Example 2
result2 = how_many_times('aaa', 'a')
print(result2)  # Output: 3

# Example 3
result3 = how_many_times('aaaa', 'aa')
print(result3)  # Output: 3
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Steps to Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the repository was cloned:
   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can run the code directly using Python. No additional installation steps are required.

## How to Use

1. **Import the Function**: Import the `how_many_times` function from the `main.py` file.

2. **Call the Function**: Use the function by passing the desired string and substring as arguments.

3. **Get the Result**: The function will return the count of overlapping occurrences of the substring in the string.

## Additional Information

- **No External Libraries**: This software is designed to be lightweight and does not require any external libraries or dependencies.
- **Python Version**: Ensure you have Python installed on your system. The software is compatible with Python 3.x versions.

For any further questions or support, please contact our support team.
```