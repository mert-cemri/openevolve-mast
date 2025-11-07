# Fruit Distribution Software

This software provides a function to calculate the number of mangoes in a basket, given the number of apples and oranges and the total number of fruits. It is a simple utility function that can be used in various applications where fruit distribution needs to be calculated.

## Main Function

### `fruit_distribution(s, n)`

- **Purpose**: Calculate the number of mangoes in a basket.
- **Parameters**:
  - `s` (str): A string containing the number of apples and oranges in the format "X apples and Y oranges".
  - `n` (int): The total number of fruits in the basket.
- **Returns**: An integer representing the number of mangoes in the basket.

#### Example Usage

```python
# Example 1
result = fruit_distribution("5 apples and 6 oranges", 19)
print(result)  # Output: 8

# Example 2
result = fruit_distribution("0 apples and 1 oranges", 3)
print(result)  # Output: 2

# Example 3
result = fruit_distribution("2 apples and 3 oranges", 100)
print(result)  # Output: 95

# Example 4
result = fruit_distribution("100 apples and 1 oranges", 120)
print(result)  # Output: 19
```

## Installation

This software does not require any external dependencies beyond the standard Python library. You can simply run the code in any Python environment.

### Quick Start

1. **Ensure Python is installed**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Clone the repository**: If you have access to a repository, clone it to your local machine. Otherwise, you can copy the `main.py` file content into your Python environment.

3. **Run the code**: Use any Python IDE or command line to run the `main.py` file.

## How to Use

1. **Import the function**: If you have the function in a separate file, make sure to import it into your script or interactive environment.

2. **Call the function**: Use the `fruit_distribution` function by passing the appropriate string and integer values as arguments.

3. **Get the result**: The function will return the number of mangoes, which you can print or use in further calculations.

## Documentation

For further details on how to use the function and integrate it into larger projects, please refer to the inline comments and docstrings within the `main.py` file. These provide additional context and examples for using the function effectively.