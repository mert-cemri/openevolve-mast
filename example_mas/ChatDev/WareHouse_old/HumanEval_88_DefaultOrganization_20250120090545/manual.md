manual.md

```
# Sort Array Application

This application provides a simple utility function to sort an array of non-negative integers based on specific criteria. The function `sort_array` sorts the array in ascending or descending order depending on the sum of the first and last elements of the array.

## Main Functionality

The main function provided by this application is `sort_array`. It operates as follows:

- **Input:** An array of non-negative integers.
- **Output:** A new sorted array based on the following rules:
  - If the sum of the first and last elements of the array is odd, the array is sorted in ascending order.
  - If the sum is even, the array is sorted in descending order.
- **Note:** The original array is not modified; a new sorted array is returned.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

This application does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository:**
   - Clone the repository to your local machine using `git clone <repository-url>`.

2. **Navigate to the Project Directory:**
   - Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Application:**
   - You can use the `sort_array` function by importing it into your Python script or interactive session.
   - Example usage:
     ```python
     from main import sort_array

     result = sort_array([2, 4, 3, 0, 1, 5])
     print(result)  # Output: [0, 1, 2, 3, 4, 5]
     ```

## Documentation

For further details on the implementation and usage, refer to the comments and docstrings within the `main.py` file. The code is straightforward and well-documented to assist in understanding the logic and functionality.

Feel free to modify and extend the code as per your requirements. If you encounter any issues or have questions, please reach out to our support team.

```