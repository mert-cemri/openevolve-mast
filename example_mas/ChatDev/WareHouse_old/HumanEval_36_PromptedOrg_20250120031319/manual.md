# Fizz Buzz Digit Counter

This software provides a function to count the number of times the digit '7' appears in integers less than a given number `n`, where those integers are divisible by either 11 or 13.

## Main Functionality

The main function of this software is:

- **fizz_buzz(n: int) -> int**: This function takes an integer `n` as input and returns the count of the digit '7' in all integers less than `n` that are divisible by 11 or 13.

### Example Usage

```python
>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

No additional installation steps are necessary since there are no external dependencies.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the function `fizz_buzz` by importing it into your Python script or interactive session.

   Example:
   ```python
   from main import fizz_buzz

   result = fizz_buzz(100)
   print(result)  # Output will be the count of '7's in numbers divisible by 11 or 13 below 100
   ```

4. **Modify and Experiment**: Feel free to modify the input value `n` to test the function with different ranges.

## Documentation

This software is simple and straightforward, designed to perform a specific task efficiently. For further information or questions, please refer to the comments within the code or contact the development team.

Enjoy using the Fizz Buzz Digit Counter!