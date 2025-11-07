# Total Match Function

This software provides a simple utility function `total_match` that compares two lists of strings and returns the list with fewer total characters. If both lists have the same number of characters, it returns the first list. This function can be useful in scenarios where you need to determine which of two datasets is smaller in terms of character count.

## Main Functionality

- **Function Name**: `total_match`
- **Purpose**: To compare two lists of strings and return the list with fewer total characters.
- **Input**: Two lists of strings.
- **Output**: The list with fewer total characters, or the first list if both have the same number of characters.

### Example Usage

```python
# Example 1
result = total_match([], [])
print(result)  # Output: []

# Example 2
result = total_match(['hi', 'admin'], ['hI', 'Hi'])
print(result)  # Output: ['hI', 'Hi']

# Example 3
result = total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
print(result)  # Output: ['hi', 'admin']

# Example 4
result = total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])
print(result)  # Output: ['hI', 'hi', 'hi']

# Example 5
result = total_match(['4'], ['1', '2', '3', '4', '5'])
print(result)  # Output: ['4']
```

## Installation

This project does not require any external dependencies, making it simple to use. You can directly use the provided `main.py` file in your Python environment.

### Steps to Use

1. **Download the Code**: Ensure you have the `main.py` file available in your project directory.

2. **Run the Code**: You can run the code using any Python interpreter. Simply import the `total_match` function and use it as demonstrated in the example usage section.

3. **No Additional Setup Required**: Since there are no external dependencies, you do not need to install any additional packages.

## Conclusion

The `total_match` function is a straightforward utility for comparing lists of strings based on their total character count. It is easy to integrate into any Python project due to its lack of dependencies and simple logic. Whether you are working with datasets or just need a quick comparison tool, this function can be a handy addition to your toolkit.