# Compare One Function

This software provides a utility function `compare_one` that compares two values, which can be integers, floats, or strings representing real numbers. The function returns the larger value in its original type or `None` if the values are equal.

## Main Functionality

### `compare_one(a, b)`

- **Purpose**: To compare two values and return the larger one in its original type.
- **Parameters**:
  - `a`: An integer, float, or string representing a real number.
  - `b`: An integer, float, or string representing a real number.
- **Returns**: The larger value in its original type, or `None` if the values are equal.

#### Examples

- `compare_one(1, 2.5)` returns `2.5`
- `compare_one(1, "2,3")` returns `"2,3"`
- `compare_one("5,1", "6")` returns `"6"`
- `compare_one("1", 1)` returns `None`

## Installation

This software does not require any external dependencies. It is implemented purely in Python and can be used directly in any Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. **Clone the Repository**: Download the code to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Code**: You can use the function in a Python script or an interactive Python session.

   ```python
   from main import compare_one

   result = compare_one(1, "2,3")
   print(result)  # Output: "2,3"
   ```

## Documentation

The function is designed to handle both standard and European decimal formats (using `.` and `,` respectively). It parses the string inputs to floats for comparison and returns the original input type for the larger value.

For further information and examples, refer to the comments within the `main.py` file. The code is straightforward and well-documented to facilitate understanding and modification if needed.