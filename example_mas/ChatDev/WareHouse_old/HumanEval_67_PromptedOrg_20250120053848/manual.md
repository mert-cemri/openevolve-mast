# Fruit Distribution Software

This software provides a simple function to calculate the number of mangoes in a basket of fruits, given a string describing the number of apples and oranges, and an integer representing the total number of fruits in the basket.

## Main Functionality

The main function of this software is `fruit_distribution`, which calculates the number of mangoes in a basket based on the provided input.

### Function: `fruit_distribution`

- **Parameters**:
  - `s` (str): A string containing the number of apples and oranges in the format "X apples and Y oranges".
  - `n` (int): An integer representing the total number of fruits in the basket.

- **Returns**:
  - `int`: The number of mangoes in the basket.

- **Example Usage**:
  ```python
  fruit_distribution("5 apples and 6 oranges", 19)  # Returns 8
  fruit_distribution("0 apples and 1 oranges", 3)   # Returns 2
  fruit_distribution("2 apples and 3 oranges", 100) # Returns 95
  fruit_distribution("100 apples and 1 oranges", 120) # Returns 19
  ```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use.

### Quick Install

Since there are no external dependencies, you can simply download the `main.py` file and run it in your Python environment.

## How to Use

1. **Download the Code**: Obtain the `main.py` file containing the `fruit_distribution` function.

2. **Run the Function**: Use the function by passing the appropriate string and integer values as arguments. You can do this in a Python script or an interactive Python session.

3. **Example**:
   ```python
   from main import fruit_distribution

   # Calculate the number of mangoes
   mangoes = fruit_distribution("5 apples and 6 oranges", 19)
   print(f"The number of mangoes is: {mangoes}")
   ```

## Documentation

For further details on how the function works, refer to the docstring within the `main.py` file. The docstring provides a comprehensive explanation of the function's parameters, return values, and example usage.

This software is designed to be simple and efficient, focusing solely on the task of calculating the number of mangoes in a basket based on the given input. Enjoy using the Fruit Distribution Software!