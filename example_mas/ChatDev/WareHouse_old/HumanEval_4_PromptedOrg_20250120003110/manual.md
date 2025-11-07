# Mean Absolute Deviation Calculator

This software provides a simple function to calculate the Mean Absolute Deviation (MAD) of a list of numbers. The Mean Absolute Deviation is a measure of statistical dispersion, representing the average absolute difference between each element in a dataset and the mean of that dataset.

## Main Function

The main function provided by this software is:

- `mean_absolute_deviation(numbers: List[float]) -> float`: This function takes a list of floating-point numbers as input and returns the Mean Absolute Deviation of the list. If the list is empty, it returns `0.0`.

## Installation

This software does not require any external dependencies beyond Python itself. To use the software, ensure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the function.

2. **Run the Function**: You can run the function in a Python environment. Here is an example of how to use the function:

    ```python
    from typing import List

    def mean_absolute_deviation(numbers: List[float]) -> float:
        """Calculate the Mean Absolute Deviation of a list of numbers."""
        if not numbers:
            return 0.0
        mean_value = sum(numbers) / len(numbers)
        absolute_deviations = [abs(x - mean_value) for x in numbers]
        mad = sum(absolute_deviations) / len(numbers)
        return mad

    # Example usage
    numbers = [1.0, 2.0, 3.0, 4.0]
    mad = mean_absolute_deviation(numbers)
    print(f"The Mean Absolute Deviation is: {mad}")
    ```

3. **Execute the Script**: Save the above code in a file named `main.py` and run it using a Python interpreter:

    ```bash
    python main.py
    ```

    This will output:

    ```
    The Mean Absolute Deviation is: 1.0
    ```

## Additional Information

- **No External Libraries Required**: The function is implemented using basic Python and does not require any additional libraries or packages.

- **Python Version**: Ensure you are using Python 3.x to avoid any compatibility issues.

This software provides a straightforward way to calculate the Mean Absolute Deviation, useful for statistical analysis and data processing tasks.