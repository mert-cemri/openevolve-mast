manual.md

```
# Sort Array Application

This application provides a simple function to sort an array of non-negative integers based on specific criteria. The function `sort_array` will sort the array in ascending order if the sum of the first and last elements is odd, or in descending order if the sum is even.

## Main Functionality

- **sort_array(array):** This function takes an array of non-negative integers as input and returns a sorted copy of the array. The sorting order is determined by the sum of the first and last elements of the array:
  - If the sum is odd, the array is sorted in ascending order.
  - If the sum is even, the array is sorted in descending order.
  - The original array is not modified.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

This application does not require any external dependencies, making it simple to set up and use. You can run the application using Python without needing to install additional packages.

### Quick Start

1. **Ensure Python is installed:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository:** If the code is hosted in a repository, clone it to your local machine using:
   ```
   git clone <repository-url>
   ```

3. **Navigate to the project directory:**
   ```
   cd <project-directory>
   ```

4. **Run the application:** You can directly use the `sort_array` function in your Python scripts or interactive shell.

## Usage

To use the `sort_array` function, simply import it into your Python script or interactive session and call it with the desired array:

```python
from main import sort_array

# Example usage
result = sort_array([2, 4, 3, 0, 1, 5])
print(result)  # Output: [0, 1, 2, 3, 4, 5]
```

This function is designed to be straightforward and efficient, providing a quick way to sort arrays based on the specified criteria.

## Documentation

For further information and examples, please refer to the code comments and docstrings within the `main.py` file. The code is self-explanatory and includes examples of how to use the function effectively.
```
