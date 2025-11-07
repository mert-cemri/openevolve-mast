manual.md

```
# How Many Times

This software provides a simple utility function to count the number of times a given substring can be found in an original string, including overlapping cases. This can be particularly useful for text analysis and processing tasks where identifying repeated patterns is necessary.

## Main Function

The main function provided by this software is `how_many_times`.

### Function: `how_many_times(string: str, substring: str) -> int`

- **Description**: This function takes two arguments: a `string` and a `substring`. It returns the number of times the `substring` appears in the `string`, including overlapping occurrences.

- **Parameters**:
  - `string` (str): The original string in which to search for the substring.
  - `substring` (str): The substring to search for within the original string.

- **Returns**: An integer representing the count of overlapping occurrences of the substring within the string.

- **Examples**:
  ```python
  >>> how_many_times('', 'a')
  0
  >>> how_many_times('aaa', 'a')
  3
  >>> how_many_times('aaaa', 'aa')
  3
  ```

## Installation

This project does not require any external dependencies, making it straightforward to set up and use.

### Quick Install

1. **Clone the Repository**: If you have access to the source code repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Move into the directory where the project files are located.

   ```bash
   cd <project-directory>
   ```

3. **Ensure Python is Installed**: Make sure you have Python installed on your system. This project is compatible with Python 3.x.

4. **No Additional Dependencies**: Since there are no external dependencies, you can directly run the Python script.

## Usage

To use the `how_many_times` function, simply import it into your Python script and call it with the desired parameters.

### Example Usage

```python
from main import how_many_times

# Example 1
result1 = how_many_times('aaa', 'a')
print(result1)  # Output: 3

# Example 2
result2 = how_many_times('aaaa', 'aa')
print(result2)  # Output: 3

# Example 3
result3 = how_many_times('', 'a')
print(result3)  # Output: 0
```

## Documentation

For further details and documentation, please refer to the docstring within the `main.py` file, which provides additional context and examples for using the `how_many_times` function.

```