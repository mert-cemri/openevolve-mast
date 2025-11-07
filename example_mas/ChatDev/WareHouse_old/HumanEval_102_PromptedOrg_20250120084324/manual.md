# Choose Num Function

This software provides a simple utility function to find the largest even integer within a specified range of two positive numbers. It is designed to be straightforward and easy to use, with minimal dependencies.

## Main Functionality

The core functionality of this software is encapsulated in the `choose_num` function, which performs the following tasks:

- **Input**: Takes two positive numbers, `x` and `y`.
- **Output**: Returns the largest even integer within the inclusive range `[x, y]`. If no even number exists within this range, it returns `-1`.

### Example Usage

- `choose_num(12, 15)` returns `14`
- `choose_num(13, 12)` returns `-1`

## Installation

This software is implemented in Python and does not require any external dependencies beyond the standard Python library. To use this function, ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: If you haven't installed Python yet, download and install it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Move into the directory containing the `main.py` file:
   ```bash
   cd <directory-name>
   ```

## How to Use

1. **Open the Python File**: Open `main.py` in your preferred code editor.

2. **Run the Function**: You can run the function directly in a Python environment or script. Here is an example of how to use it:

   ```python
   from main import choose_num

   result = choose_num(12, 15)
   print(result)  # Output: 14
   ```

3. **Modify Inputs**: Change the input values `x` and `y` in the function call to test different ranges.

## Documentation

For further details on Python programming and standard library functions, refer to the official [Python documentation](https://docs.python.org/3/).

This software is designed to be simple and efficient, providing a quick solution to find the largest even number within a given range. If you encounter any issues or have suggestions for improvements, please feel free to contribute or contact the development team.