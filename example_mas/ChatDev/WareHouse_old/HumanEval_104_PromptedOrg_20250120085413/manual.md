# Unique Digits Software

This software provides a function to filter and sort a list of positive integers, returning only those numbers that do not contain any even digits. The returned list is sorted in increasing order.

## Main Functionality

The core functionality of this software is encapsulated in the `unique_digits` function. This function takes a list of positive integers and returns a sorted list of numbers that do not have any even digits.

### Example Usage

```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the code is located.
   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: You can run the code using Python.
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you are using this function in another script, import it.
   ```python
   from main import unique_digits
   ```

2. **Call the Function**: Pass a list of positive integers to the `unique_digits` function.
   ```python
   result = unique_digits([15, 33, 1422, 1])
   print(result)  # Output: [1, 15, 33]
   ```

## Documentation

The function `unique_digits` is designed to be simple and straightforward. It uses a helper function `has_even_digit` to check if a number contains any even digits. The main function filters out numbers with even digits and returns a sorted list of the remaining numbers.

For further details on the implementation, refer to the comments within the code in `main.py`.

## Support

For any issues or questions, please contact the development team at [support@chatdev.com](mailto:support@chatdev.com). We are here to help you with any problems you might encounter.