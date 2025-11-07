# Truncate Number Software

This software provides a simple utility function to extract the decimal part of a given positive floating point number. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The main function of this software is `truncate_number`, which takes a positive floating point number as input and returns the decimal part of that number. For example, if the input is `3.5`, the function will return `0.5`.

### Function Definition

```python
def truncate_number(number: float) -> float:
    """Return the decimal part of the number."""
    return number - int(number)
```

### Example Usage

```python
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## How to Use

1. **Download the Code**: Save the provided code snippet into a file named `main.py`.

2. **Run the Code**: Open a terminal or command prompt, navigate to the directory containing `main.py`, and execute the following command:

   ```bash
   python main.py
   ```

   This will run the example usage of the `truncate_number` function, demonstrating its functionality.

3. **Modify for Your Needs**: You can modify the `main.py` file to use the `truncate_number` function with different inputs as needed for your application.

## Conclusion

This software provides a straightforward solution for extracting the decimal part of a floating point number. Its simplicity and lack of dependencies make it easy to integrate into larger projects or use as a standalone utility.