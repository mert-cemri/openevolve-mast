# Rescale to Unit

This software module provides a function to rescale a list of numbers to the unit interval [0, 1]. It is designed to transform any given list of numbers such that the smallest number becomes 0 and the largest becomes 1, with all other numbers scaled proportionally in between.

## Main Functionality

The main function provided by this module is `rescale_to_unit`. This function takes a list of floating-point numbers and applies a linear transformation to rescale the numbers to the range [0, 1].

### Function Signature

```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
```

### Parameters

- `numbers`: A list of floating-point numbers. The list must contain at least two elements.

### Returns

- A list of floating-point numbers rescaled to the unit interval [0, 1].

### Example Usage

```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```

## Installation

This project does not require any external dependencies, making it straightforward to set up and use.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python environment. Simply ensure that you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Start by cloning the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Move into the directory containing the `main.py` file.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can use the function by importing it into your Python script or interactive session.

   ```python
   from main import rescale_to_unit

   numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   rescaled_numbers = rescale_to_unit(numbers)
   print(rescaled_numbers)
   ```

4. **Test the Function**: You can test the function with different lists of numbers to ensure it behaves as expected.

## Documentation

For further information and detailed documentation, please refer to the inline comments and docstrings within the `main.py` file. These provide additional context and examples for using the `rescale_to_unit` function effectively.

Feel free to reach out for support or contribute to the project if you have any suggestions or improvements.