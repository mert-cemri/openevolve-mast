# Sum Squares Function

This software provides a simple utility function to compute the sum of squares of a list of numbers, where each number is first rounded up to the nearest integer (using the ceiling function).

## Main Functionality

The main function provided by this software is `sum_squares(lst)`. This function takes a list of numbers as input and returns the sum of the squares of these numbers after rounding each number up to the nearest integer.

### Example Usage

```python
from main import sum_squares

# Example list of numbers
numbers = [1.4, 4.2, 0]

# Calculate the sum of squares
result = sum_squares(numbers)

print(result)  # Output: 29
```

### Function Details

- **Input:** A list of numbers (integers or floats).
- **Output:** An integer representing the sum of the squares of the numbers after rounding each to the nearest upper integer.

### Examples

- For `lst = [1, 2, 3]`, the output will be `14`.
- For `lst = [1, 4, 9]`, the output will be `98`.
- For `lst = [1, 3, 5, 7]`, the output will be `84`.
- For `lst = [1.4, 4.2, 0]`, the output will be `29`.
- For `lst = [-2.4, 1, 1]`, the output will be `6`.

## Installation

To use this software, you need to have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/).

### Environment Setup

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change your current directory to the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies:**

   This project does not have any external dependencies, so you can directly use the provided Python script.

## Usage

Once you have set up your environment, you can use the `sum_squares` function by importing it into your Python script or interactive session.

```python
from main import sum_squares

# Example usage
numbers = [1.4, 4.2, 0]
result = sum_squares(numbers)
print(result)  # Output: 29
```

## Documentation

For further details and documentation, please refer to the comments within the `main.py` file, which provide additional context and examples for using the `sum_squares` function.