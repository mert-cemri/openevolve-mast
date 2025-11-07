manual.md

```
# Choose Number Application

This application provides a simple function to determine the largest even integer within a specified range of two positive numbers. It is designed to be lightweight and does not require any external dependencies.

## Main Functionality

The core functionality of this application is encapsulated in the `choose_num` function. This function takes two positive integers, `x` and `y`, and returns the largest even integer within the inclusive range `[x, y]`. If no even number exists within the range, the function returns `-1`.

### Function Signature

```python
def choose_num(x, y):
    """
    This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.
    """
```

### Examples

- `choose_num(12, 15)` returns `14`
- `choose_num(13, 12)` returns `-1`

## Installation

Since this application does not require any external libraries, you can use it directly without any additional installation steps. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can test the function by running a Python interpreter and calling the `choose_num` function with your desired inputs.

### Example Usage

```bash
$ python
>>> from main import choose_num
>>> result = choose_num(12, 15)
>>> print(result)  # Output: 14
```

## No External Dependencies

This application is designed to be simple and efficient, requiring no external Python packages. It runs on any standard Python environment.

## Conclusion

The Choose Number Application is a straightforward tool for finding the largest even number within a given range. Its simplicity and lack of dependencies make it easy to integrate into other projects or use as a standalone utility.
```