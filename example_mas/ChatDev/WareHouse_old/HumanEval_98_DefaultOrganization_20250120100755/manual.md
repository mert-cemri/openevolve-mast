# Count Upper

This software provides a simple function to count the number of uppercase vowels located at even indices in a given string. It is implemented in Python and is designed to be lightweight with no external dependencies.

## Main Functionality

The main function provided by this software is `count_upper(s)`. This function takes a single argument, `s`, which is a string, and returns the count of uppercase vowels ('A', 'E', 'I', 'O', 'U') that appear at even indices in the string.

### Example Usage

```python
count_upper('aBCdEf')  # Returns 1
count_upper('abcdefg')  # Returns 0
count_upper('dBBE')     # Returns 0
```

## Installation

Since this software does not require any external dependencies, you can use it directly in your Python environment. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `count_upper` function.

2. **Run the Function**: You can use the function in your Python scripts or interactive environment. Simply import the function and pass a string to it.

   ```python
   from main import count_upper

   result = count_upper('YourStringHere')
   print(result)
   ```

3. **Testing**: You can test the function with different strings to ensure it behaves as expected.

## Documentation

The function is straightforward and does not require additional configuration. It iterates over the string, checking only the even indices for uppercase vowels and counting them.

For further assistance or inquiries, please contact our support team or refer to the comments within the code for more details on its implementation.