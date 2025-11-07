# Change Base Function

This software provides a simple utility function to convert a given integer from base 10 to another numerical base less than 10. The function is implemented in Python and is designed to be used in various applications where base conversion is required.

## Main Functionality

The main function provided by this software is `change_base(x: int, base: int) -> str`. This function takes two arguments:
- `x`: An integer in base 10 that you want to convert.
- `base`: The target base to which you want to convert the integer. The base must be less than 10.

The function returns a string representation of the number in the new base.

### Example Usage

```python
result = change_base(8, 3)
print(result)  # Output: '22'

result = change_base(8, 2)
print(result)  # Output: '1000'

result = change_base(7, 2)
print(result)  # Output: '111'
```

## Installation

This software does not require any external dependencies, making it easy to integrate into your existing Python projects. You can simply copy the `change_base` function into your codebase.

## How to Use

1. **Copy the Function**: Copy the `change_base` function from the provided `main.py` file into your Python script or module.

2. **Call the Function**: Use the function by passing the integer you want to convert and the target base as arguments.

3. **Handle the Output**: The function will return a string that represents the number in the new base. You can print this string or use it in further computations.

## Example Code

Here's a simple example of how you might use the `change_base` function in a Python script:

```python
def change_base(x: int, base: int) -> str:
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))
        x = x // base
    digits.reverse()
    return ''.join(digits)

# Example usage
if __name__ == "__main__":
    number = 8
    new_base = 3
    converted_number = change_base(number, new_base)
    print(f"The number {number} in base {new_base} is {converted_number}.")
```

This example demonstrates how to convert the number 8 to base 3, resulting in the output '22'.

## Notes

- Ensure that the base provided is less than 10, as the function is not designed to handle bases equal to or greater than 10.
- The function handles the conversion of positive integers only. Negative numbers and non-integer inputs are not supported.