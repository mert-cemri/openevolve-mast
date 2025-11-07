manual.md

```
# How Many Times

A Python utility to count the number of times a given substring appears in a string, including overlapping occurrences.

## Overview

The `how_many_times` function is designed to find and count all occurrences of a specified substring within a given string, including cases where the occurrences overlap. This can be particularly useful in text analysis and processing tasks where precise substring counting is required.

## Main Function

### how_many_times(string: str, substring: str) -> int

- **Description**: This function takes two arguments: a `string` and a `substring`. It returns an integer representing the number of times the `substring` is found within the `string`, counting overlapping occurrences.

- **Parameters**:
  - `string` (str): The original string in which to search for the substring.
  - `substring` (str): The substring to search for within the original string.

- **Returns**: An integer count of how many times the `substring` appears in the `string`, including overlapping cases.

- **Example Usage**:
  ```python
  >>> how_many_times('', 'a')
  0
  >>> how_many_times('aaa', 'a')
  3
  >>> how_many_times('aaaa', 'aa')
  3
  ```

## Installation

### Environment Setup

This utility does not require any external dependencies beyond standard Python libraries. Ensure you have Python installed on your system.

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

3. **Ensure Python is Installed**: Verify that Python is installed by running:
   ```bash
   python --version
   ```

## Usage

1. **Run the Function**: You can directly use the function in your Python scripts by importing it from the `main.py` file.

   ```python
   from main import how_many_times

   # Example usage
   result = how_many_times('aaaa', 'aa')
   print(result)  # Output: 3
   ```

2. **Testing**: You can test the function using the provided examples or by writing additional test cases to ensure it meets your specific needs.

## Documentation and Support

For further assistance or to report issues, please contact our support team or visit our documentation page (if available).

```

This manual provides a comprehensive guide on how to use the `how_many_times` function, including installation instructions and example usage. It is designed to help users quickly understand and implement the function in their own projects.