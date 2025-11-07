# Filter by Substring

This software provides a simple utility function to filter a list of strings based on the presence of a specified substring. It is designed to be straightforward and efficient, making it easy to integrate into larger projects or use as a standalone tool.

## Main Functionality

The primary function of this software is `filter_by_substring`, which takes a list of strings and a substring as input and returns a list of strings that contain the specified substring.

### Function Signature

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
```

### Example Usage

```python
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
```

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine. Otherwise, download the `main.py` file.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Code**: You can run the code directly using Python.

```bash
python main.py
```

## How to Use

1. **Import the Function**: If you are integrating this function into another project, simply import it.

```python
from main import filter_by_substring
```

2. **Call the Function**: Use the function by passing a list of strings and the substring you want to filter by.

```python
result = filter_by_substring(['example', 'test', 'sample'], 'ex')
print(result)  # Output: ['example']
```

## Documentation

For further details on how to use the function, refer to the docstring within the `main.py` file. The docstring provides examples and a brief explanation of the function's purpose and usage.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the code comments.