# Mean Absolute Deviation Calculator

This software module provides a function to calculate the Mean Absolute Deviation (MAD) of a list of numbers. The Mean Absolute Deviation is a measure of statistical dispersion, representing the average absolute difference between each element and the mean of the dataset.

## Main Function

The main function provided by this module is:

- `mean_absolute_deviation(numbers: List[float]) -> float`: This function takes a list of floating-point numbers as input and returns the Mean Absolute Deviation of the numbers. If the input list is empty, the function returns `0.0`.

### Example Usage

```python
from main import mean_absolute_deviation

numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0
```

## Installation

This module does not require any external dependencies, making it simple to set up and use. You can directly use the function in your Python environment.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file to your local machine.

2. **Set Up Environment**: Ensure you have Python installed on your system. This module is compatible with Python 3.x.

3. **Run the Code**: You can directly run the code in your Python environment or integrate it into your existing Python projects.

## How to Use

1. **Import the Function**: Import the `mean_absolute_deviation` function from the `main.py` file.

2. **Prepare Your Data**: Create a list of floating-point numbers that you want to calculate the Mean Absolute Deviation for.

3. **Call the Function**: Pass your list of numbers to the `mean_absolute_deviation` function to get the MAD value.

4. **Interpret the Results**: The function returns a floating-point number representing the Mean Absolute Deviation of the input list.

## Documentation

For further details and documentation, please refer to the docstring provided within the `main.py` file. The docstring includes a description of the function, its parameters, and an example usage.

This module is designed to be straightforward and easy to integrate into any Python project that requires statistical analysis of numerical data.