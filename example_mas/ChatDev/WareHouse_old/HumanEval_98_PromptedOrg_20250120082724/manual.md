# Count Upper

This software provides a simple utility function to count the number of uppercase vowels located at even indices within a given string. It is designed to be lightweight and does not require any external dependencies.

## Main Function

### `count_upper(s)`

- **Description**: This function takes a string `s` as input and returns the number of uppercase vowels ('A', 'E', 'I', 'O', 'U') that are located at even indices in the string.
  
- **Parameters**: 
  - `s` (str): The input string to be analyzed.

- **Returns**: 
  - `int`: The count of uppercase vowels at even indices.

- **Examples**:
  - `count_upper('aBCdEf')` returns `1`
  - `count_upper('abcdefg')` returns `0`
  - `count_upper('dBBE')` returns `0`

## Installation

This software does not require any external libraries or dependencies. It is implemented purely in Python and can be used in any Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. No additional installation steps are required since there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where the `main.py` file is located.

3. You can use the function `count_upper` by importing it into your Python script or by running it directly in an interactive Python session.

### Example Usage

```python
from main import count_upper

# Example strings
example1 = 'aBCdEf'
example2 = 'abcdefg'
example3 = 'dBBE'

# Count uppercase vowels at even indices
result1 = count_upper(example1)
result2 = count_upper(example2)
result3 = count_upper(example3)

print(f"Uppercase vowels in '{example1}' at even indices: {result1}")
print(f"Uppercase vowels in '{example2}' at even indices: {result2}")
print(f"Uppercase vowels in '{example3}' at even indices: {result3}")
```

4. Run your script or enter the commands in a Python interactive shell to see the results.

## Documentation

For further information on Python and its capabilities, please refer to the official [Python documentation](https://docs.python.org/3/). This will provide you with comprehensive guidance on Python programming, including string manipulation and other standard library functions.