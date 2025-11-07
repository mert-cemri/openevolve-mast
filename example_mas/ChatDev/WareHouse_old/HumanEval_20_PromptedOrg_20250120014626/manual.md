# Find Closest Elements

This software provides a function to find and return the two closest numbers from a supplied list of floating-point numbers. The function ensures that the numbers are returned in order, with the smaller number first.

## Main Functionality

The main function provided by this software is `find_closest_elements`. It takes a list of floating-point numbers as input and returns a tuple containing the two closest numbers from the list.

### Function Signature

```python
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
```

### Example Usage

```python
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
(2.0, 2.2)

>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
(2.0, 2.0)
```

## Installation

To use this software, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly use the provided code.

### Steps to Install Python

1. **Download Python**: Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**: Run the installer and follow the installation instructions. Make sure to check the option to add Python to your system's PATH.

3. **Verify Installation**: Open a terminal or command prompt and type `python --version` to verify that Python is installed correctly.

## How to Use

1. **Copy the Code**: Copy the provided code for the `find_closest_elements` function into a Python file, e.g., `main.py`.

2. **Run the Code**: Open a terminal or command prompt, navigate to the directory containing `main.py`, and run the file using the command:

   ```bash
   python main.py
   ```

3. **Test the Function**: You can test the function by calling it with different lists of numbers and observing the output.

## Documentation

The function is straightforward and does not require additional libraries or complex setup. It sorts the list of numbers and iterates through them to find the pair with the smallest difference.

For further information or support, you can refer to Python's official documentation or reach out to the development team for assistance.