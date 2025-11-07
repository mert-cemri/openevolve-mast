# Mean Absolute Deviation Calculator

This software provides a simple function to calculate the Mean Absolute Deviation (MAD) of a list of numbers. The Mean Absolute Deviation is a measure of statistical dispersion, representing the average absolute difference between each element in a dataset and the mean of that dataset.

## Main Function

The main function provided by this software is `mean_absolute_deviation`, which calculates the Mean Absolute Deviation for a given list of floating-point numbers.

### Function Signature

```python
def mean_absolute_deviation(numbers: List[float]) -> float:
```

### Parameters

- `numbers` (List[float]): A list of floating-point numbers for which the Mean Absolute Deviation is to be calculated.

### Returns

- `float`: The Mean Absolute Deviation of the list.

### Example Usage

```python
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
```

## Installation

This project does not require any external dependencies. It is implemented using Python's standard library. To use the function, simply ensure you have Python installed on your system.

### Quick Install

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone or download the repository containing the `main.py` file.

3. **Run the Code**: You can run the code directly using a Python interpreter.

## How to Use

1. **Open a Python Environment**: You can use any Python environment, such as IDLE, PyCharm, or a simple command-line interface.

2. **Import the Function**: Import the `mean_absolute_deviation` function from the `main.py` file.

3. **Call the Function**: Pass a list of floating-point numbers to the function and receive the Mean Absolute Deviation.

### Example

```python
from main import mean_absolute_deviation

numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation is: {mad}")
```

## Documentation

For further details on how the Mean Absolute Deviation is calculated, refer to the docstring provided in the `main.py` file. This includes a detailed explanation of the formula used and the logic behind the implementation.

This software is designed to be simple and efficient, providing a quick way to calculate statistical dispersion in datasets without the need for complex installations or dependencies.