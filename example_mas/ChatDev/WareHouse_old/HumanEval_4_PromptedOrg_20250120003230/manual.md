# Mean Absolute Deviation Calculator

This software provides a simple function to calculate the Mean Absolute Deviation (MAD) of a list of numbers. The Mean Absolute Deviation is a measure of variability that represents the average absolute difference between each element in a dataset and the mean of the dataset.

## Main Function

The main function provided by this software is `mean_absolute_deviation`, which takes a list of floating-point numbers as input and returns the Mean Absolute Deviation as a floating-point number.

### Function Definition

```python
def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate the Mean Absolute Deviation of a list of numbers."""
    if not numbers:
        return 0.0
    # Calculate the mean of the numbers
    mean_value = sum(numbers) / len(numbers)
    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(x - mean_value) for x in numbers]
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(numbers)
    return mad
```

### Example Usage

```python
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
```

## Installation

This software does not require any external dependencies. You can simply copy the `main.py` file to your project and use the `mean_absolute_deviation` function as needed.

## How to Use

1. **Copy the Code**: Copy the function definition from the `main.py` file into your Python project.

2. **Import the Function**: If you have saved the function in a separate file, make sure to import it into your main script.

3. **Call the Function**: Use the `mean_absolute_deviation` function by passing a list of floating-point numbers as an argument.

4. **Get the Result**: The function will return the Mean Absolute Deviation of the provided list.

## Notes

- The function returns `0.0` if the input list is empty.
- The input list should contain floating-point numbers for accurate results.

This software is designed to be simple and efficient, providing a quick way to calculate the Mean Absolute Deviation for any dataset you are working with.