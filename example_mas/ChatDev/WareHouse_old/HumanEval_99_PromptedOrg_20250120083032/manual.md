# Closest Integer Function

This software provides a simple Python function to determine the closest integer to a given numeric string input. The function is designed to round numbers away from zero when they are equidistant from two integers.

## Main Functionality

The main function of this software is `closest_integer(value)`, which takes a string representing a number and returns the closest integer. The rounding strategy used is "away from zero" for numbers that are equidistant from two integers.

### Examples

- `closest_integer("10")` returns `10`
- `closest_integer("15.3")` returns `15`
- `closest_integer("14.5")` returns `15`
- `closest_integer("-14.5")` returns `-15`

## Installation

This project does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the code in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

## How to Use

1. **Open the `main.py` file**: This file contains the `closest_integer` function.

2. **Run the Function**: You can test the function by calling it with different string inputs. For example:
   ```python
   print(closest_integer("10"))  # Output: 10
   print(closest_integer("15.3"))  # Output: 15
   print(closest_integer("14.5"))  # Output: 15
   print(closest_integer("-14.5"))  # Output: -15
   ```

3. **Modify as Needed**: You can modify the `main.py` file to include additional test cases or integrate it into a larger application.

## Documentation

This function is straightforward and does not require extensive documentation. However, if you need to understand the logic behind the rounding strategy, refer to the comments within the `main.py` file.

For any further questions or support, please contact the development team.