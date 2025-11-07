# Sort Array Application

This application provides a function to sort an array of non-negative integers based on specific criteria. The array is sorted in ascending order if the sum of the first and last elements is odd, and in descending order if the sum is even. This functionality is useful for various computational tasks where conditional sorting is required.

## Main Functionality

The main function provided by this application is `sort_array(array)`. This function takes an array of non-negative integers as input and returns a sorted copy of the array based on the following rules:

- If the sum of the first and last elements of the array is odd, the array is sorted in ascending order.
- If the sum is even, the array is sorted in descending order.
- The original array remains unchanged.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

To use this application, you need to have Python installed on your system. The application does not require any additional dependencies, so you can directly use the provided code.

### Quick Install

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file containing the `sort_array` function.

3. No additional packages are required, so you can directly run the Python script.

## How to Use

1. Open your terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python script using the command:
   ```bash
   python main.py
   ```

4. You can call the `sort_array` function within the script or import it into another Python script to use it with different arrays.

## Documentation

For further details on how the function works, refer to the comments within the `main.py` file. The function is straightforward and does not require any additional configuration or setup.

Feel free to modify the code to suit your specific needs or integrate it into larger projects where conditional sorting is required.