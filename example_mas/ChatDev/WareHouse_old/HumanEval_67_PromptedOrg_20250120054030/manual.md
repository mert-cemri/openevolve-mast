# Fruit Distribution Software

This software provides a function to calculate the number of mango fruits in a basket, given a string describing the number of apples and oranges, and an integer representing the total number of fruits in the basket.

## Main Functionality

The main function of this software is:

- **`fruit_distribution(s, n)`**: This function takes two parameters:
  - `s` (str): A string that represents the number of apples and oranges.
  - `n` (int): An integer that represents the total number of fruits in the basket.
  
  It returns the number of mango fruits in the basket by extracting the numbers of apples and oranges from the string and subtracting them from the total number of fruits.

## Installation

This software does not require any external dependencies, so you can use it directly without installing additional packages. However, ensure you have Python installed on your system.

### Steps to Install Python

1. **Download Python**: Go to the official [Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**: Follow the instructions provided on the website to install Python on your system.

3. **Verify Installation**: Open a terminal or command prompt and type `python --version` to verify that Python is installed correctly.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `fruit_distribution` function.

2. **Run the Function**: You can run the function by executing the `main.py` file in a Python environment. Here is an example of how to use the function:

   ```python
   from main import fruit_distribution

   # Example usage
   result = fruit_distribution("5 apples and 6 oranges", 19)
   print("Number of mango fruits:", result)  # Output: Number of mango fruits: 8
   ```

3. **Modify as Needed**: You can modify the input string and total number of fruits to suit your needs and test different scenarios.

## Example Scenarios

- `fruit_distribution("5 apples and 6 oranges", 19)` returns `8`.
- `fruit_distribution("0 apples and 1 oranges", 3)` returns `2`.
- `fruit_distribution("2 apples and 3 oranges", 100)` returns `95`.
- `fruit_distribution("100 apples and 1 oranges", 120)` returns `19`.

This software provides a simple yet effective way to calculate the number of mango fruits in a basket, based on the given input parameters.