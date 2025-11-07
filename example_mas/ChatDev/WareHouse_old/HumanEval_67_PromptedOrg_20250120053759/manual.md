manual.md

```
# Fruit Distribution Calculator

This software provides a simple function to calculate the number of mango fruits in a basket, given a string that describes the number of apples and oranges, and an integer representing the total number of fruits in the basket.

## Main Functionality

The main function of this software is `fruit_distribution`, which calculates the number of mango fruits in a basket. The function takes two inputs:
- A string `s` that specifies the number of apples and oranges in the format "X apples and Y oranges".
- An integer `n` that represents the total number of fruits in the basket.

The function returns the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits.

### Example Usage

```python
from main import fruit_distribution

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

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Steps to Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your working directory to the cloned repository:
   ```
   cd <repository-directory>
   ```

3. **Run the Code**: You can directly run the code using Python as shown in the example usage above.

## Environment Dependencies

There are no external dependencies required for this project. The function is implemented using standard Python libraries.

## Documentation

For further details on how the function works, refer to the docstring provided in the `main.py` file. The docstring explains the parameters, return values, and provides examples of how to use the function.

```