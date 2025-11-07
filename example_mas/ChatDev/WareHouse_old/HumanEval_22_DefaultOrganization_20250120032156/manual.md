# Filter Integers Application

This application provides a simple utility function to filter integers from a list of various Python values. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this application is provided by the `filter_integers` function. This function takes a list of any Python values and returns a new list containing only the integer values from the original list.

### Function Signature

```python
def filter_integers(values: List[Any]) -> List[int]:
```

### Example Usage

```python
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
```

## Installation

This application does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Project Directory**: Open a terminal and navigate to the directory where the repository is located.

3. **Run the Code**: You can directly run the `main.py` file to test the function.

```bash
python main.py
```

## How to Use

1. **Import the Function**: If you want to use the function in another Python script, you can import it as follows:

```python
from main import filter_integers
```

2. **Call the Function**: Pass a list of values to the `filter_integers` function to get a list of integers.

```python
result = filter_integers(['a', 3.14, 5, 7, 'hello'])
print(result)  # Output: [5, 7]
```

## Documentation

For further details on how to use the function, refer to the docstring provided within the code. The docstring includes example usage and expected outputs.

This application is designed to be simple and straightforward, with a focus on filtering integer values from a mixed list of Python objects. Enjoy using the Filter Integers Application!