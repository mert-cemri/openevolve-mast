# Truncate Number

This software provides a simple utility function to extract the decimal part of a given positive floating point number. It is designed to be lightweight and does not require any external dependencies.

## Main Functionality

The main function of this software is:

- **truncate_number(number: float) -> float**: This function takes a positive floating point number as input and returns the decimal part of the number. For example, if the input is `3.5`, the function will return `0.5`.

## Installation

Since this project does not require any external dependencies, you do not need to install any additional packages. You only need to have Python installed on your system.

### Prerequisites

- **Python**: Ensure that you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```

3. **Run the Function**: You can use the function by importing it into your Python script or by running it directly in a Python shell. Here is an example of how to use it in a Python script:
   ```python
   from main import truncate_number

   result = truncate_number(3.5)
   print(result)  # Output: 0.5
   ```

4. **Testing**: You can test the function with different floating point numbers to ensure it works as expected.

## Example Usage

Here is a simple example of how to use the `truncate_number` function:

```python
from main import truncate_number

# Example 1
number1 = 3.5
decimal_part1 = truncate_number(number1)
print(f"The decimal part of {number1} is {decimal_part1}")

# Example 2
number2 = 10.75
decimal_part2 = truncate_number(number2)
print(f"The decimal part of {number2} is {decimal_part2}")
```

This will output:

```
The decimal part of 3.5 is 0.5
The decimal part of 10.75 is 0.75
```

## Conclusion

This software provides a straightforward utility to extract the decimal part of a floating point number. It is easy to use and does not require any additional setup beyond having Python installed. Feel free to integrate this function into your projects where such functionality is needed.