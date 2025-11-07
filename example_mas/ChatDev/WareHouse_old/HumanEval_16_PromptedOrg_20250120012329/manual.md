```markdown
# Count Distinct Characters

This software provides a simple utility function to count the number of distinct characters in a given string, regardless of their case. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function provided by this software is:

- `count_distinct_characters(string: str) -> int`: This function takes a string as input and returns the number of distinct characters in the string, ignoring case. For example:
  - `count_distinct_characters('xyzXYZ')` returns `3`
  - `count_distinct_characters('Jerry')` returns `4`

## Installation

Since this software does not require any external dependencies, you only need to have Python installed on your system to run it. Follow these steps to set up your environment:

1. **Install Python**: Ensure that Python is installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your working directory to the location where the code is stored:
   ```bash
   cd <directory-name>
   ```

## Usage

To use the `count_distinct_characters` function, follow these steps:

1. **Open a Python Environment**: You can use a Python interactive shell or a script to run the function.

2. **Import the Function**: If the function is in a file named `main.py`, you can import it as follows:
   ```python
   from main import count_distinct_characters
   ```

3. **Call the Function**: Pass a string to the function and receive the count of distinct characters:
   ```python
   result = count_distinct_characters('HelloWorld')
   print(result)  # Output will be 7
   ```

## Example

Here is a simple example of how to use the function in a Python script:

```python
from main import count_distinct_characters

# Example usage
string = "HelloWorld"
distinct_count = count_distinct_characters(string)
print(f"The number of distinct characters in '{string}' is {distinct_count}.")
```

## Conclusion

This utility is a straightforward tool for counting distinct characters in a string, useful for various text processing tasks. It is easy to integrate into larger projects or use as a standalone script.
```
