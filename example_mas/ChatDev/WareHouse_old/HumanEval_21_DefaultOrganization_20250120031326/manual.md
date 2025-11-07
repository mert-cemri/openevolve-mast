# Rescale to Unit

This software module provides a function to rescale a list of numbers to a unit scale, where the smallest number in the list becomes 0 and the largest becomes 1. This is useful for normalizing data for various applications such as machine learning, data analysis, and visualization.

## Main Function

### `rescale_to_unit(numbers: List[float]) -> List[float]`

- **Description**: This function takes a list of floating-point numbers and applies a linear transformation to rescale the numbers. The smallest number in the list is transformed to 0, and the largest number is transformed to 1. All other numbers are scaled proportionally between 0 and 1.
  
- **Parameters**: 
  - `numbers`: A list of floating-point numbers with at least two elements.

- **Returns**: 
  - A list of floating-point numbers rescaled to the unit interval [0, 1].

- **Example Usage**:
  ```python
  >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
  [0.0, 0.25, 0.5, 0.75, 1.0]
  ```

## Quick Install

This module does not require any external dependencies, making it straightforward to use in any Python environment.

### Installation

1. **Clone the Repository**: If the code is hosted in a version control system, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory containing the `main.py` file.

   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: Since there are no external dependencies, you can directly run the Python script.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you want to use the function in another script, import it from the module.

   ```python
   from main import rescale_to_unit
   ```

2. **Call the Function**: Pass a list of numbers to the function and receive the rescaled list.

   ```python
   numbers = [10.0, 20.0, 30.0, 40.0, 50.0]
   rescaled_numbers = rescale_to_unit(numbers)
   print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
   ```

## Documentation

For further details and examples, please refer to the inline documentation within the `main.py` file. The function is designed to be simple and intuitive, with a focus on ease of use and integration into larger projects.