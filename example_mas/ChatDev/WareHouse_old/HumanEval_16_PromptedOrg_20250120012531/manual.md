# Count Distinct Characters

This software provides a simple function to count the number of distinct characters in a given string, regardless of their case. It is implemented in Python and is designed to be straightforward and easy to use.

## Main Function

The main function of this software is:

- **count_distinct_characters(string: str) -> int**: This function takes a string as input and returns the number of distinct characters in the string, ignoring case. For example:
  - `count_distinct_characters('xyzXYZ')` returns `3`
  - `count_distinct_characters('Jerry')` returns `4`

## Installation

### Environment Setup

To use this software, you need to have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

### Dependencies

This software does not require any additional Python packages or dependencies beyond the standard library. Therefore, there is no need for a `requirements.txt` file.

## Usage

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your current directory to the location where the repository is cloned.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can use the function by importing it into your Python script or interactive session.

   ```python
   from main import count_distinct_characters

   # Example usage
   print(count_distinct_characters('xyzXYZ'))  # Output: 3
   print(count_distinct_characters('Jerry'))   # Output: 4
   ```

## Documentation

The function is documented with examples in the docstring. You can view the documentation by using Python's built-in help function.

```python
help(count_distinct_characters)
```

This will display the function's docstring, which includes a brief description and examples of how to use the function.

## Conclusion

This software provides a simple and efficient way to count distinct characters in a string, ignoring case. It is easy to integrate into any Python project and does not require any external dependencies.