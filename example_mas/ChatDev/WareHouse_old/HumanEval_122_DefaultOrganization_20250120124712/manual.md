# Add Elements Software

This software provides a simple function to calculate the sum of elements with at most two digits from the first `k` elements of a given array of integers. It is designed to be efficient and easy to use, with no external dependencies required.

## Main Functionality

The main function provided by this software is `add_elements(arr, k)`. This function takes two parameters:
- `arr`: A non-empty list of integers.
- `k`: An integer representing the number of elements from the start of the list to consider.

The function returns the sum of the elements that have at most two digits (i.e., values between -99 and 99 inclusive) from the first `k` elements of the array.

### Example

```python
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
print(add_elements(arr, k))  # Output: 24
```

In this example, the function considers the first 4 elements of the array `[111, 21, 3, 4000]`. Among these, only `21` and `3` have at most two digits, so their sum, `24`, is returned.

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Script**: Execute the script using Python to see the function in action.

```bash
python main.py
```

## Usage

To use the `add_elements` function in your own projects, simply import the function from the `main.py` file and call it with your desired parameters.

### Example Usage

```python
from main import add_elements

arr = [50, 60, 70, 80, 90]
k = 3
result = add_elements(arr, k)
print(f"The sum of elements with at most two digits is: {result}")
```

This will output:

```
The sum of elements with at most two digits is: 180
```

## Documentation

For further details on how the function works, refer to the comments within the `main.py` file. The function is designed to be intuitive and easy to integrate into larger projects.

If you encounter any issues or have questions, feel free to reach out for support.