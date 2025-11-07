# Rounded Average Function

This software provides a simple Python function, `rounded_avg`, which calculates the average of integers between two given numbers, rounds the result to the nearest integer, and converts it to a binary string. If the first number is greater than the second, it returns -1.

## Main Function

### `rounded_avg(n, m)`

- **Description**: Computes the average of integers from `n` to `m` (inclusive), rounds it to the nearest integer, and converts the result to a binary string. If `n` is greater than `m`, it returns -1.
- **Parameters**:
  - `n` (int): The starting integer.
  - `m` (int): The ending integer.
- **Returns**:
  - A binary string representing the rounded average, or -1 if `n` is greater than `m`.

### Example Usage

```python
result1 = rounded_avg(1, 5)  # Returns "0b11"
result2 = rounded_avg(7, 5)  # Returns -1
result3 = rounded_avg(10, 20)  # Returns "0b1111"
result4 = rounded_avg(20, 33)  # Returns "0b11010"
```

## Installation

### Environment Setup

No external dependencies are required for this software. You can run the code in any Python environment. Below are the steps to set up a basic Python environment:

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Virtual Environment (Optional but Recommended)**:
   - Open a terminal or command prompt.
   - Navigate to your project directory.
   - Run the following command to create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies**:
   - Since there are no external dependencies, you can skip this step.

## How to Use

1. **Clone the Repository** (if applicable):
   - Use `git clone` to clone the repository to your local machine.

2. **Navigate to the Project Directory**:
   - Use the terminal or command prompt to navigate to the directory containing `main.py`.

3. **Run the Code**:
   - Open `main.py` in your preferred code editor.
   - Use the function `rounded_avg(n, m)` as demonstrated in the example usage section.
   - Run the script using Python:
     ```bash
     python main.py
     ```

## Documentation

For further details on the implementation and usage of the `rounded_avg` function, please refer to the comments within the `main.py` file. The function is self-contained and does not require additional modules or packages.