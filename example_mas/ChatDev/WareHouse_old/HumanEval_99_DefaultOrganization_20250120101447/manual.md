# Closest Integer Function

This software provides a simple Python function to determine the closest integer to a given numerical value represented as a string. The function handles rounding in a specific manner, rounding away from zero when the number is equidistant from two integers.

## Main Functionality

The main functionality of this software is encapsulated in the `closest_integer` function. This function takes a string input representing a number and returns the closest integer to that number. The rounding strategy used is as follows:

- If the number is equidistant from two integers, the function rounds away from zero. For example:
  - `closest_integer("14.5")` returns `15`
  - `closest_integer("-14.5")` returns `-15`

## Installation

This project does not require any external dependencies, so you can run it with a standard Python installation. Ensure you have Python installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/downloads/).

## Usage

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the project directory.

   ```bash
   cd <project-directory>
   ```

3. **Run the Script**: You can run the script directly using Python. The script includes example usage of the `closest_integer` function.

   ```bash
   python main.py
   ```

4. **Using the Function**: You can use the `closest_integer` function in your own Python scripts by importing it from `main.py`.

   ```python
   from main import closest_integer

   result = closest_integer("15.3")
   print(result)  # Output: 15
   ```

## Example Usage

The `main.py` script includes example usage of the `closest_integer` function. When you run the script, it will print the results of several test cases:

```python
if __name__ == "__main__":
    print(closest_integer("10"))    # Output: 10
    print(closest_integer("15.3"))  # Output: 15
    print(closest_integer("14.5"))  # Output: 15
    print(closest_integer("-14.5")) # Output: -15
```

These examples demonstrate how the function handles different inputs, including positive and negative numbers, as well as numbers that are equidistant from two integers.

## Documentation

For further details on the function and its implementation, please refer to the comments within the `main.py` file. The code is straightforward and well-documented to facilitate understanding and modification if necessary.