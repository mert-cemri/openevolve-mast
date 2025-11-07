# Even Odd Palindrome Counter

This software provides a function to count the number of even and odd integer palindromes within a given range. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function of this software is `even_odd_palindrome(n)`, which takes a positive integer `n` as input and returns a tuple containing the number of even and odd integer palindromes from 1 to `n`, inclusive.

### How It Works

- **Palindrome Check**: The function checks if a number is a palindrome by converting it to a string and comparing it to its reverse.
- **Even and Odd Count**: It iterates through each number in the range, checks if it is a palindrome, and then determines if it is even or odd to update the respective count.

## Installation

This software does not require any external libraries or dependencies. It is implemented purely in Python, so you only need to have Python installed on your system.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

To use the `even_odd_palindrome` function, follow these steps:

1. **Open a Python Environment**: You can use any Python environment like IDLE, PyCharm, or simply the command line.

2. **Define the Function**: Copy the function code into your Python environment.

    ```python
    def even_odd_palindrome(n):
        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]
        even_count = 0
        odd_count = 0
        for i in range(1, n + 1):
            if is_palindrome(i):
                if i % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
        return (even_count, odd_count)
    ```

3. **Call the Function**: Use the function by passing a positive integer `n` as an argument.

    ```python
    result = even_odd_palindrome(12)
    print(result)  # Output: (4, 6)
    ```

## Example

Here is an example of how to use the function:

```python
# Example usage
n = 12
result = even_odd_palindrome(n)
print(f"The number of even and odd palindromes between 1 and {n} are: {result}")
```

This will output:

```
The number of even and odd palindromes between 1 and 12 are: (4, 6)
```

## Documentation

For further documentation and examples, refer to the comments within the code. The function is straightforward and designed for ease of use without additional setup or configuration.