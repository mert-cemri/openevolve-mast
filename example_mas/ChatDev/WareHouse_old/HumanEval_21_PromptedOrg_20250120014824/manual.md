# Rescale to Unit

This software provides a simple function to rescale a list of numbers to a unit scale, where the smallest number becomes 0 and the largest becomes 1. This is useful for normalizing data for various applications such as machine learning, data analysis, and visualization.

## Main Function

The main function provided by this software is `rescale_to_unit`. It takes a list of floating-point numbers and returns a new list where the numbers are linearly transformed to fit within the range [0, 1].

### Function Signature

```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
```

### Example Usage

```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```

## Installation

This software does not require any external dependencies, making it easy to integrate into your existing Python projects.

### Quick Install

Since there are no external dependencies, you can simply copy the `main.py` file into your project directory and import the `rescale_to_unit` function as needed.

## How to Use

1. **Copy the Code**: Copy the `main.py` file into your project directory.

2. **Import the Function**: In your Python script, import the `rescale_to_unit` function.

    ```python
    from main import rescale_to_unit
    ```

3. **Call the Function**: Pass a list of floating-point numbers to the function to get the rescaled list.

    ```python
    numbers = [10.0, 20.0, 30.0, 40.0, 50.0]
    rescaled_numbers = rescale_to_unit(numbers)
    print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
    ```

## Documentation

The function is straightforward and does not require additional configuration or setup. It is designed to be used in any Python environment where basic list operations are supported.

For further assistance or questions, please contact our support team.