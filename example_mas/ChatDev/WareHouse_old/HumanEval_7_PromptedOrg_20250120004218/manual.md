# Filter by Substring

This software provides a simple utility function to filter a list of strings based on the presence of a specified substring. It is designed to be straightforward and efficient, requiring no external dependencies.

## Main Function

The main function of this software is `filter_by_substring`, which filters an input list of strings to only include those that contain a specified substring.

### Function Signature

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
```

### Parameters

- `strings` (List[str]): The list of strings to filter.
- `substring` (str): The substring to search for within each string.

### Returns

- List[str]: A list of strings that contain the specified substring.

### Examples

```python
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory containing the `main.py` file.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Script**: You can run the script directly using Python.

   ```bash
   python main.py
   ```

## Usage

To use the `filter_by_substring` function, you can import it into your Python script and call it with the desired parameters.

### Example Usage

```python
from main import filter_by_substring

strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
filtered_strings = filter_by_substring(strings, substring)
print(filtered_strings)  # Output: ['abc', 'bacd', 'array']
```

## Documentation

For further documentation and examples, please refer to the docstring within the `main.py` file. The function is well-documented with examples to help you understand its usage.

This software is designed to be simple and efficient, providing a utility function that can be easily integrated into larger projects or used standalone for quick filtering tasks.