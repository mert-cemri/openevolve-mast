# Closest Integer Function

This software provides a simple Python function to determine the closest integer to a given numerical string input. The function is designed to handle rounding away from zero when the number is equidistant from two integers.

## Main Functionality

The primary function of this software is:

- **`closest_integer(value)`**: This function takes a string input representing a number and returns the closest integer. If the number is equidistant from two integers, it rounds away from zero.

### Examples

- `closest_integer("10")` returns `10`
- `closest_integer("15.3")` returns `15`
- `closest_integer("14.5")` returns `15`
- `closest_integer("-14.5")` returns `-15`

## Installation

This project does not require any external dependencies. You only need Python installed on your system to run the function.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Project Directory**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can test the function by running the `main.py` file in your terminal or command prompt. Use the following command:

   ```bash
   python main.py
   ```

   You can also directly call the `closest_integer` function within a Python script or an interactive Python session by importing the function.

4. **Example Usage**: You can test the function with different inputs by modifying the example usage section in the `main.py` file or by calling the function in an interactive Python session.

```python
# Example usage:
print(closest_integer("10"))  # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("14.5"))  # Output: 15
print(closest_integer("-14.5"))  # Output: -15
```

## Documentation

For further documentation and examples, refer to the comments within the `main.py` file. The function is straightforward and designed to be easily integrated into other Python projects.

Feel free to reach out for support or contribute to the project by submitting issues or pull requests on the project's repository.