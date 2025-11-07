# Fruit Distribution Software

This software provides a simple function to calculate the number of mango fruits in a basket, given a string that describes the number of apples and oranges, and an integer representing the total number of fruits in the basket.

## Main Function

### `fruit_distribution(s, n)`

- **Description**: This function calculates the number of mango fruits in a basket.
- **Parameters**:
  - `s` (str): A string containing the number of apples and oranges in the format "X apples and Y oranges".
  - `n` (int): The total number of fruits in the basket.
- **Returns**: An integer representing the number of mango fruits in the basket.

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

This software does not require any external dependencies, making it straightforward to set up and use.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Run the Software**: You can run the software directly using Python as there are no additional dependencies to install.

## How to Use

1. **Prepare Your Environment**: Ensure you have Python installed on your machine. This software is compatible with Python 3.x.

2. **Run the Function**: Use the `fruit_distribution` function by importing it into your Python script or interactive session.

3. **Input the Parameters**: Provide the string describing the number of apples and oranges, and the integer for the total number of fruits.

4. **Get the Result**: The function will return the number of mango fruits in the basket.

## Documentation

For further details on using the function, refer to the comments and docstrings within the `main.py` file. The code is self-explanatory and designed to be easy to understand and integrate into your projects.

This software is designed to be simple and efficient, providing a straightforward solution to the problem of calculating the number of mangoes in a fruit basket. Enjoy using the software!