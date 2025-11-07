# Fruit Distribution Software

This software module calculates the number of mango fruits in a basket given a string describing the number of apples and oranges, and an integer representing the total number of fruits.

## Main Functionality

The main function of this software is to determine the number of mangoes in a fruit basket. It takes two inputs:
- A string that specifies the number of apples and oranges.
- An integer that represents the total number of fruits in the basket.

The function then calculates and returns the number of mangoes by subtracting the number of apples and oranges from the total number of fruits.

## Installation

This software does not require any external dependencies. It is implemented in Python and can be run in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download and install Python from the official [Python website](https://www.python.org/).

## Usage

To use the software, follow these steps:

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

2. **Run the Function**: Open a Python environment and import the `fruit_distribution` function from the `main.py` file.

3. **Example Usage**:
    ```python
    from main import fruit_distribution

    # Example 1
    result1 = fruit_distribution("5 apples and 6 oranges", 19)
    print(result1)  # Output: 8

    # Example 2
    result2 = fruit_distribution("0 apples and 1 oranges", 3)
    print(result2)  # Output: 2

    # Example 3
    result3 = fruit_distribution("2 apples and 3 oranges", 100)
    print(result3)  # Output: 95

    # Example 4
    result4 = fruit_distribution("100 apples and 1 oranges", 120)
    print(result4)  # Output: 19
    ```

## Documentation

The function is straightforward and does not require additional documentation beyond the examples provided. It is designed to be simple and efficient, focusing solely on the task of calculating the number of mangoes in a basket based on the given inputs.

For any further questions or support, please contact the development team.