# Sort Array Application

This application provides a function to sort an array of non-negative integers based on the sum of the first and last elements of the array. The sorting order is determined by whether the sum is odd or even.

## Main Functionality

The main function of this application is `sort_array`, which performs the following operations:

- **Input:** An array of non-negative integers.
- **Output:** A sorted copy of the input array.
  - If the sum of the first and last elements of the array is odd, the array is sorted in ascending order.
  - If the sum is even, the array is sorted in descending order.
- **Note:** The original array is not modified.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

This application does not require any external dependencies, so you can use it directly with a standard Python installation.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository:**
   - Clone the repository to your local machine using Git or download the ZIP file and extract it.

2. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Application:**
   - You can use the `sort_array` function by importing it into your Python script or by running it directly in a Python interactive shell.

4. **Example Usage:**
   ```python
   from main import sort_array

   # Example arrays
   print(sort_array([]))  # Output: []
   print(sort_array([5]))  # Output: [5]
   print(sort_array([2, 4, 3, 0, 1, 5]))  # Output: [0, 1, 2, 3, 4, 5]
   print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # Output: [6, 5, 4, 3, 2, 1, 0]
   ```

## Documentation

For further details and examples, please refer to the comments within the `main.py` file. The function is straightforward and does not require additional libraries or complex setup.

Feel free to modify and extend the functionality as needed for your specific use case.