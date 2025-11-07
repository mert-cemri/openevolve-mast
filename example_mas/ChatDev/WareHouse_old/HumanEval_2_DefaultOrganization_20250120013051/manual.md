```markdown
# Truncate Number Application

This application provides a simple function to extract the decimal part of a given positive floating point number. It is designed to be straightforward and efficient, requiring no external dependencies.

## Main Functionality

The core functionality of this application is encapsulated in the `truncate_number` function. This function takes a positive floating point number as input and returns the decimal part of that number. For example, if the input is `3.5`, the function will return `0.5`.

### Function Definition

```python
def truncate_number(number: float) -> float:
    """Return the decimal part of the given positive floating point number."""
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
```

### Example Usage

To use the function, you can call it directly with a floating point number:

```python
print(truncate_number(3.5))  # Output: 0.5
```

## Installation

This application does not require any external Python packages, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the source code by cloning the repository or downloading it as a ZIP file.

3. **Navigate to the project directory**: Open a terminal or command prompt and change to the directory where the source code is located.

## Running the Application

To run the application and see the `truncate_number` function in action, execute the `main.py` file:

```bash
python main.py
```

This will print the result of the example usage, demonstrating the function's capability to extract the decimal part of a floating point number.

## Documentation

For further information or to contribute to the project, please refer to the source code and comments within the `main.py` file. The code is designed to be self-explanatory and easy to understand.

Feel free to modify and extend the functionality as needed for your specific use cases.
```
```