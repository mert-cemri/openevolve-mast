# Unique Digits Software

This software provides a function to filter and return a sorted list of integers that do not contain any even digits. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function provided by this software is `unique_digits`, which takes a list of positive integers and returns a sorted list of those integers that do not contain any even digits.

### Function: `unique_digits`

- **Input**: A list of positive integers.
- **Output**: A sorted list of integers from the input that do not contain any even digits.

#### Example Usage

```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]

>>> unique_digits([152, 323, 1422, 10])
[]
```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the repository is located.

3. **Run the Code**: Use Python to run the `main.py` file.

```bash
python main.py
```

## How to Use

1. **Import the Function**: If you are integrating this function into another project, you can import it directly.

```python
from main import unique_digits
```

2. **Call the Function**: Pass a list of positive integers to the `unique_digits` function to get the desired output.

```python
result = unique_digits([15, 33, 1422, 1])
print(result)  # Output: [1, 15, 33]
```

## Documentation

For further details on the implementation and usage of the `unique_digits` function, please refer to the comments within the `main.py` file. The function is designed to be self-explanatory and easy to integrate into other Python projects.

Feel free to reach out if you have any questions or need further assistance with using this software.