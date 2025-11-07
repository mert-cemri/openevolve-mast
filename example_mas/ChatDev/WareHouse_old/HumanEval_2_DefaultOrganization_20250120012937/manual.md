manual.md

```
# Truncate Number

A simple Python utility to extract the decimal part of a given positive floating point number.

## Overview

The `truncate_number` function is designed to take a positive floating point number as input and return its decimal part. This can be useful in various applications where only the fractional part of a number is needed.

### Main Function

- **truncate_number(number: float) -> float**: This function takes a single argument, `number`, which is a positive floating point number. It returns the decimal part of the number by subtracting the integer part from the original number.

#### Example Usage

```python
>>> truncate_number(3.5)
0.5
```

## Installation

### Prerequisites

- Python 3.x

### Quick Install

Since there are no external dependencies required for this utility, you can directly use the function in your Python environment. Simply copy the function code into your Python script or interactive environment.

## How to Use

1. **Copy the Code**: Copy the `truncate_number` function from the `main.py` file into your Python script or interactive environment.

2. **Call the Function**: Use the function by passing a positive floating point number as an argument.

   ```python
   result = truncate_number(4.75)
   print(result)  # Output will be 0.75
   ```

3. **Integrate into Projects**: You can integrate this function into larger projects where you need to handle floating point numbers and extract their decimal parts.

## Documentation

This utility is straightforward and does not require additional documentation beyond the function's docstring and the example provided. For any further assistance, consider exploring Python's standard library documentation for related functions and operations.

```

This manual provides a comprehensive guide on how to use the `truncate_number` function, including installation instructions and usage examples. Since the function is self-contained and does not require external dependencies, the installation section is simplified.