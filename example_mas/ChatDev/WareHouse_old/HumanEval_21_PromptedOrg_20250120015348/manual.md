# Rescale to Unit

This software module provides a function to rescale a list of numbers such that the smallest number becomes 0 and the largest becomes 1. This is useful for normalizing data to a standard range, which can be beneficial in various data processing and machine learning tasks.

## Main Function

### `rescale_to_unit`

- **Description**: This function takes a list of floating-point numbers and applies a linear transformation to rescale the numbers. The smallest number in the list is transformed to 0, and the largest number is transformed to 1. All other numbers are scaled proportionally between 0 and 1.

- **Parameters**: 
  - `numbers` (List[float]): A list of floating-point numbers with at least two elements.

- **Returns**: 
  - List[float]: A list of numbers rescaled to the range [0, 1].

- **Example**:
  ```python
  >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
  [0.0, 0.25, 0.5, 0.75, 1.0]
  ```

## Installation

This module does not require any external dependencies beyond the standard Python library. Ensure you have Python installed on your system.

## Usage

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can use the function by importing it into your Python script or interactive session. Here's an example of how to use it:

   ```python
   from main import rescale_to_unit

   numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   rescaled_numbers = rescale_to_unit(numbers)
   print(rescaled_numbers)
   ```

4. **Testing**: You can test the function using the provided example or by passing your own list of numbers.

## Documentation

For further information and detailed documentation, please refer to the docstring within the `main.py` file. This includes a description of the function, its parameters, and an example of its usage.

## Support

For any questions or issues, please contact the development team at ChatDev. We are here to assist you with any inquiries related to the software.