# Sort Array Application

This application provides a function to sort an array of non-negative integers based on specific criteria. The function `sort_array` sorts the array in ascending or descending order depending on the sum of the first and last elements of the array.

## Main Functionality

The main function of this application is `sort_array`, which performs the following operations:

- **Input**: An array of non-negative integers.
- **Output**: A sorted copy of the input array.
  - If the sum of the first and last elements of the array is odd, the array is sorted in ascending order.
  - If the sum is even, the array is sorted in descending order.
- The original array remains unchanged.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

To use this application, ensure you have Python installed on your system. This application does not require any additional dependencies beyond the Python standard library.

### Quick Install

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change into the directory containing the `main.py` file.

   ```bash
   cd <directory-name>
   ```

## How to Use

1. **Open the Python File**: Open the `main.py` file in your preferred code editor.

2. **Run the Function**: You can test the `sort_array` function by calling it with different arrays. For example:

   ```python
   from main import sort_array

   print(sort_array([2, 4, 3, 0, 1, 5]))  # Output: [0, 1, 2, 3, 4, 5]
   print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # Output: [6, 5, 4, 3, 2, 1, 0]
   ```

3. **Execute the Script**: Run the script using Python to see the results.

   ```bash
   python main.py
   ```

## Documentation

For further information and detailed documentation, please refer to the comments within the `main.py` file. The function is well-documented to provide clarity on its usage and behavior.

## Support

For any issues or questions, please contact our support team or open an issue in the repository. We are here to help you make the most out of this application.