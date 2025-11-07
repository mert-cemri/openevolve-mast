# Common Elements Finder

This software provides a simple utility function to find and return the sorted unique common elements from two lists. It is designed to be lightweight and does not require any external dependencies.

## Main Functionality

The main function of this software is:

- **common(l1: list, l2: list) -> list**: This function takes two lists as input and returns a sorted list of unique elements that are common to both lists.

### Example Usage

```python
# Example 1
result = common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
print(result)  # Output: [1, 5, 653]

# Example 2
result = common([5, 3, 2, 8], [3, 2])
print(result)  # Output: [2, 3]
```

## Installation

This software does not require any external libraries or dependencies, so there is no need for a `requirements.txt` file. You can simply use the function in your Python environment.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can use the function directly in your Python scripts or interactive environment.

   ```python
   from main import common

   # Use the function as demonstrated in the example usage section.
   ```

## Documentation

The function is straightforward and does not require additional documentation. The docstring within the function provides examples of how to use it.

For any further inquiries or support, please contact our support team.