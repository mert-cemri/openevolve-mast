# Sort Array Application

This application provides a function to sort an array of non-negative integers based on specific criteria. The sorting order is determined by the sum of the first and last elements of the array.

## Main Functionality

The main function provided by this application is `sort_array(array)`. This function takes an array of non-negative integers and returns a sorted copy of the array based on the following rules:

- If the sum of the first and last elements of the array is odd, the array is sorted in ascending order.
- If the sum is even, the array is sorted in descending order.
- The original array is not modified.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

This application does not require any external dependencies. You can use it directly with Python.

### Quick Start

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change to the directory containing the `main.py` file:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Application:**

   You can run the application using Python:

   ```bash
   python main.py
   ```

## Usage

To use the `sort_array` function, you can import it into your Python script and call it with the desired array:

```python
from main import sort_array

# Example usage
result = sort_array([2, 4, 3, 0, 1, 5])
print(result)  # Output: [0, 1, 2, 3, 4, 5]
```

## Documentation

For further details on how to use the function and examples, refer to the comments within the `main.py` file. The function is straightforward and does not require additional setup or configuration.

Feel free to modify and integrate the function into your projects as needed.