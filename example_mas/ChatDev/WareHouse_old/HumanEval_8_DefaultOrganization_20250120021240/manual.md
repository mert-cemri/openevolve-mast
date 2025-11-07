```markdown
# SumProduct Application

This application provides a simple utility function to calculate the sum and product of a list of integers. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this application is encapsulated in the `sum_product` function. This function takes a list of integers as input and returns a tuple containing the sum and the product of the integers in the list. If the list is empty, it returns a sum of 0 and a product of 1.

### Function Signature

```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
```

### Example Usage

```python
>>> sum_product([])
(0, 1)

>>> sum_product([1, 2, 3, 4])
(10, 24)
```

## Installation

Since this application does not require any external libraries, there is no need to install additional dependencies. You can simply download the `main.py` file and run it in any Python environment.

## How to Use

1. **Download the Code**: Obtain the `main.py` file containing the `sum_product` function.

2. **Run the Function**: You can use the function in any Python script by importing it. Here's an example:

    ```python
    from main import sum_product

    result = sum_product([1, 2, 3, 4])
    print(result)  # Output: (10, 24)
    ```

3. **Testing**: You can test the function using Python's built-in `doctest` module to ensure it works as expected:

    ```bash
    python -m doctest main.py
    ```

This will run the examples provided in the docstring and verify that the function behaves correctly.

## Documentation

For further details on how the function works, please refer to the docstring within the `main.py` file. The docstring provides a clear explanation of the function's purpose, input parameters, and expected output.

Feel free to modify and extend the code to suit your specific needs. The simplicity of the code makes it easy to integrate into larger projects or adapt for different use cases.
```