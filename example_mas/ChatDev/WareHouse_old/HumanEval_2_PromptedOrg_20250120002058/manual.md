# Truncate Number Function

This software provides a simple Python function to extract the decimal part of a given positive floating-point number. The function is designed to be straightforward and efficient, making it suitable for various applications where such functionality is required.

## Main Functionality

The main function provided by this software is `truncate_number`, which takes a positive floating-point number as input and returns its decimal part. For example, if the input is `3.5`, the function will return `0.5`.

### Function Definition

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)
```

## Installation

This software does not require any external dependencies, making it easy to integrate into any Python environment.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python project. Simply copy the function definition into your Python script or module.

## How to Use

1. **Copy the Function**: Copy the `truncate_number` function definition into your Python script.

2. **Call the Function**: Use the function by passing a positive floating-point number as an argument. For example:

    ```python
    result = truncate_number(3.5)
    print(result)  # Output: 0.5
    ```

3. **Integration**: You can integrate this function into larger projects where you need to process or analyze floating-point numbers and require the decimal part.

## Example Usage

Here is a simple example demonstrating how to use the `truncate_number` function:

```python
# Example usage of truncate_number function
def main():
    number = 7.89
    decimal_part = truncate_number(number)
    print(f"The decimal part of {number} is {decimal_part}")

if __name__ == "__main__":
    main()
```

This example will output:

```
The decimal part of 7.89 is 0.89
```

## Conclusion

The `truncate_number` function is a simple yet effective tool for extracting the decimal part of a floating-point number. With no external dependencies, it is easy to use and integrate into any Python project.