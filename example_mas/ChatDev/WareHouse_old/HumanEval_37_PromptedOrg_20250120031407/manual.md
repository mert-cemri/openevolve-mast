# Sort Even Indices Function

This software provides a simple utility function to sort the elements of a list that are located at even indices, while keeping the elements at odd indices unchanged. This can be useful in various data processing tasks where specific ordering of elements is required.

## Main Functionality

The main function provided by this software is `sort_even`. It takes a list as input and returns a new list where the elements at even indices are sorted, while the elements at odd indices remain in their original order.

### Function Signature

```python
def sort_even(l: list) -> list:
```

### Example Usage

```python
# Example 1
result = sort_even([1, 2, 3])
print(result)  # Output: [1, 2, 3]

# Example 2
result = sort_even([5, 6, 3, 4])
print(result)  # Output: [3, 6, 5, 4]
```

## Installation

This software does not require any external dependencies, making it easy to integrate into your existing Python environment.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python scripts without any additional installation steps.

## How to Use

1. **Copy the Code**: Copy the `sort_even` function from the `main.py` file into your Python script.

2. **Call the Function**: Use the `sort_even` function by passing a list of numbers as an argument. The function will return a new list with the even-indexed elements sorted.

3. **Example**: Refer to the example usage section above to see how to call the function and handle its output.

## Documentation

For further details and examples, refer to the comments within the `main.py` file. The function is straightforward and designed to be easily understood and integrated into your projects.

Feel free to modify the function to suit your specific needs or to extend its functionality as required.