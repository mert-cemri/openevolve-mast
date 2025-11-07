# Truncate Number Software

This software provides a simple function to extract the decimal part of a given positive floating point number. It is designed to be straightforward and efficient, focusing on the core functionality without any additional features or interfaces.

## Main Functionality

The primary function of this software is:

- **truncate_number(number: float) -> float**: This function takes a positive floating point number as input and returns the decimal part of that number. For example, if the input is `3.5`, the function will return `0.5`.

## Installation

This software does not require any external dependencies, making it easy to set up and use. However, you need to have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

### Quick Install

1. **Clone the Repository**: You can clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to the cloned repository:
   ```bash
   cd <repository-directory>
   ```

3. **Run the Script**: You can run the script using Python:
   ```bash
   python main.py
   ```

## Usage

To use the `truncate_number` function, you can simply call it with a positive floating point number as an argument. Here is an example of how to use the function:

```python
from main import truncate_number

# Example usage
result = truncate_number(3.5)
print(result)  # Output: 0.5
```

This will print the decimal part of the number `3.5`, which is `0.5`.

## Documentation

The function is documented within the code using a docstring, which provides a brief description of the function's purpose and an example of its usage. You can access this documentation by using Python's built-in help function:

```python
help(truncate_number)
```

This will display the docstring, giving you a quick overview of how the function works and how to use it.

## Conclusion

This software is designed to be a simple and efficient tool for extracting the decimal part of a floating point number. With no external dependencies, it is easy to set up and use, making it a convenient solution for this specific task.