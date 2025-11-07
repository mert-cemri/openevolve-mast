# Rounded Average Calculator

This software provides a function `rounded_avg` that calculates the average of integers from `n` to `m`, rounds it to the nearest integer, and converts the result to a binary string. If `n` is greater than `m`, the function returns `-1`.

## Main Functionality

- **Function Name**: `rounded_avg`
- **Purpose**: Computes the average of integers between two given numbers, rounds the result, and converts it to a binary string.
- **Parameters**:
  - `n`: A positive integer representing the starting point of the range.
  - `m`: A positive integer representing the ending point of the range.
- **Returns**:
  - A binary string representation of the rounded average if `n` is less than or equal to `m`.
  - `-1` if `n` is greater than `m`.

### Example Usage

```python
rounded_avg(1, 5)  # Returns: "0b11"
rounded_avg(7, 5)  # Returns: -1
rounded_avg(10, 20)  # Returns: "0b1111"
rounded_avg(20, 33)  # Returns: "0b11010"
```

## Installation

### Prerequisites

- Python 3.x installed on your system.

### Steps

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Although there are no external dependencies listed in the `requirements.txt` file, ensure your Python environment is set up correctly.

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is empty, you can skip this step.

## How to Use

1. **Open the `main.py` File**: Locate the `main.py` file in your project directory.

2. **Import the Function**: Use the function in your Python script or interactive shell.

   ```python
   from main import rounded_avg
   ```

3. **Call the Function**: Pass the desired values of `n` and `m` to the function.

   ```python
   result = rounded_avg(1, 5)
   print(result)  # Output: "0b11"
   ```

## Additional Information

- Ensure that the input values for `n` and `m` are positive integers.
- The function handles cases where `n` is greater than `m` by returning `-1`.

This software provides a simple yet effective way to calculate and convert averages to binary, making it useful for various computational tasks.