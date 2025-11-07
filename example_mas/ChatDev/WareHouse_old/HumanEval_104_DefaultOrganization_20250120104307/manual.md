# Unique Digits Software

This software provides a function to filter and sort a list of positive integers, returning only those numbers that do not contain any even digits. The function is useful for applications where such filtering is necessary.

## Main Functionality

The main function provided by this software is `unique_digits(x)`, which takes a list of positive integers and returns a sorted list of integers that do not contain any even digits. The returned list is sorted in increasing order.

### Example Usage

```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

## Installation

This software does not require any external dependencies, so there is no need for additional installations beyond having Python installed on your system.

### Quick Setup

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the repository or download the `main.py` file**: Ensure you have the `main.py` file in your working directory.

3. **Run the function**: You can use the function directly in your Python environment by importing it from `main.py`.

## How to Use

1. **Import the function**: In your Python script or interactive environment, import the `unique_digits` function.

    ```python
    from main import unique_digits
    ```

2. **Call the function with a list of integers**: Pass a list of positive integers to the function to get the filtered and sorted list.

    ```python
    result = unique_digits([15, 33, 1422, 1])
    print(result)  # Output: [1, 15, 33]
    ```

3. **Interpret the results**: The function will return a list of integers that do not contain any even digits, sorted in increasing order.

## Additional Information

- **No external libraries**: This software is designed to be lightweight and does not require any additional Python packages.
- **Python version**: Ensure you are using a compatible version of Python (Python 3.x is recommended).

For any further questions or support, please contact our development team. We are committed to providing assistance and ensuring the software meets your needs.