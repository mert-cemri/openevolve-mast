manual.md

```
# Pluck Function

This software provides a simple utility function called `pluck` that is designed to work with arrays of non-negative integers. The primary purpose of this function is to identify and return the smallest even number from the array, along with its index. If no even numbers are present, it returns an empty list.

## Main Functionality

### pluck(arr)

- **Description**: 
  - This function takes an array of non-negative integers and returns the smallest even number along with its index in the array.
  - If there are multiple occurrences of the smallest even number, the function returns the one with the smallest index.
  - If the array is empty or contains no even numbers, the function returns an empty list.

- **Parameters**:
  - `arr`: A list of non-negative integers.

- **Returns**:
  - A list containing two elements: `[smallest_even_value, index]`.
  - Returns an empty list `[]` if no even numbers are found or if the input array is empty.

- **Examples**:
  - `pluck([4, 2, 3])` returns `[2, 1]`
  - `pluck([1, 2, 3])` returns `[2, 1]`
  - `pluck([])` returns `[]`
  - `pluck([5, 0, 3, 0, 4, 2])` returns `[0, 1]`

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file containing the `pluck` function.

3. No additional packages are required, so you can directly use the function in your Python environment.

## Usage

1. Open your Python environment or script where you want to use the `pluck` function.

2. Import the function from the `main.py` file:
   ```python
   from main import pluck
   ```

3. Call the `pluck` function with your desired array:
   ```python
   result = pluck([4, 2, 3])
   print(result)  # Output: [2, 1]
   ```

4. You can test the function with different arrays to see how it behaves with various inputs.

## Documentation

For further details on the function's logic and examples, refer to the comments within the `main.py` file. The function is designed to be intuitive and easy to integrate into larger projects where array manipulation is required.

```