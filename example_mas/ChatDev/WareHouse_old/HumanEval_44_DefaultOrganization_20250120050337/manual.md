# Change Base Software

This software provides a simple utility function to convert a given non-negative integer from base 10 to another numerical base, where the base is between 2 and 9. This is useful for applications that require base conversion for numbers, such as in computer science and digital electronics.

## Main Functionality

The main functionality of this software is encapsulated in the `change_base` function. This function takes two parameters:

- `x` (int): The non-negative integer that you want to convert.
- `base` (int): The base to which you want to convert the number. This must be between 2 and 9.

The function returns a string representation of the number in the specified base.

### Example Usage

```python
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

## Installation

This software does not require any external dependencies, making it straightforward to use. You can simply copy the `main.py` file to your project directory.

### Requirements

There are no additional packages required to run this software. It is implemented using standard Python libraries.

## How to Use

1. **Copy the Code**: Ensure that you have the `main.py` file in your project directory.

2. **Run the Code**: You can execute the code directly using Python. Open a terminal or command prompt, navigate to the directory containing `main.py`, and run:

   ```bash
   python main.py
   ```

3. **Modify for Custom Use**: You can modify the `main.py` file to include other numbers and bases you wish to convert by changing the parameters in the `change_base` function calls.

## Error Handling

The function includes basic error handling to ensure that the inputs are valid:

- The number `x` must be non-negative.
- The `base` must be between 2 and 9.

If these conditions are not met, the function will raise a `ValueError`.

## Conclusion

This software provides a simple and efficient way to convert numbers from base 10 to another base between 2 and 9. It is easy to integrate into other projects due to its lack of external dependencies and straightforward functionality.