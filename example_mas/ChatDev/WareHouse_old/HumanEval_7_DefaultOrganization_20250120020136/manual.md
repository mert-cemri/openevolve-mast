manual.md

```
# Filter by Substring

A simple Python utility to filter a list of strings based on the presence of a given substring.

## Overview

This software provides a single function, `filter_by_substring`, which allows users to filter an input list of strings, returning only those strings that contain a specified substring. This can be useful in various applications where string filtering is required.

## Main Function

### `filter_by_substring`

- **Purpose**: Filters an input list of strings to include only those that contain a specified substring.
- **Parameters**:
  - `strings` (List[str]): A list of strings to be filtered.
  - `substring` (str): The substring to filter the strings by.
- **Returns**: A list of strings that contain the specified substring.

#### Example Usage

```python
from main import filter_by_substring

# Example 1: Empty list
result = filter_by_substring([], 'a')
print(result)  # Output: []

# Example 2: List with strings containing 'a'
result = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
print(result)  # Output: ['abc', 'bacd', 'array']
```

## Installation

### Environment Setup

This project does not require any external dependencies, making it straightforward to set up and run. You only need Python installed on your system.

1. **Ensure Python is installed**: You can download Python from the official [Python website](https://www.python.org/downloads/).

2. **Clone the repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the script**: You can directly run the script using Python.
   ```bash
   python main.py
   ```

## Usage

To use the `filter_by_substring` function, simply import it into your Python script and call it with the appropriate parameters as shown in the example usage section.

## Documentation

For more detailed documentation and examples, please refer to the inline comments and docstrings within the `main.py` file.

```