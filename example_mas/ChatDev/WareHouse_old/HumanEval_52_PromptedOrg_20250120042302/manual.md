# Below Threshold Function

This software provides a simple utility function to check if all numbers in a given list are below a specified threshold. It is implemented in Python and is designed to be straightforward and easy to use.

## Main Function

### below_threshold

The `below_threshold` function takes a list of numbers and a threshold value as input and returns `True` if all numbers in the list are below the threshold, otherwise it returns `False`.

#### Function Signature

```python
def below_threshold(l: list, t: int) -> bool:
```

#### Parameters

- `l` (list): A list of numbers to be checked.
- `t` (int): The threshold value.

#### Returns

- `bool`: Returns `True` if all numbers in the list are below the threshold, otherwise `False`.

#### Example Usage

```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```

## Installation

To use this function, you need to have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can run the function by executing the `main.py` file in a Python environment.

   ```bash
   python main.py
   ```

4. **Test the Function**: You can test the function by calling it with different lists and threshold values as shown in the example usage.

## Dependencies

This function does not require any external libraries or dependencies beyond the standard Python library.

## Documentation

For further details and documentation, please refer to the comments within the `main.py` file. The function is well-documented with examples to help you understand its usage.

Feel free to reach out if you have any questions or need further assistance.