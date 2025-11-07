manual.md

```
# SpecialFilter

SpecialFilter is a Python function designed to filter numbers based on specific criteria. It counts the number of elements in an array that are greater than 10 and have both their first and last digits as odd numbers (1, 3, 5, 7, 9).

## Main Functionality

The main function provided by this software is `specialFilter(nums)`. This function takes a list of numbers as input and returns the count of numbers that meet the specified criteria.

### Function Details

- **Function Name:** `specialFilter`
- **Input:** A list of integers.
- **Output:** An integer representing the count of numbers that are greater than 10 and have both first and last digits as odd.

### Example Usage

```python
result1 = specialFilter([15, -73, 14, -15])
print(result1)  # Output: 1

result2 = specialFilter([33, -2, -3, 45, 21, 109])
print(result2)  # Output: 2
```

## Installation

This software does not require any external dependencies, making it straightforward to use. You only need Python installed on your machine.

### Quick Install

1. **Ensure Python is installed:** You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository:** You can clone the repository using Git or download the ZIP file and extract it.

3. **Navigate to the directory:** Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

## How to Use

1. **Open the terminal or command prompt.**

2. **Navigate to the directory containing `main.py`.**

3. **Run the Python script:**

   ```bash
   python main.py
   ```

4. **Modify the `specialFilter` function call in `main.py` to test with different inputs.**

## Documentation

For further details on how the function works, please refer to the comments within the `main.py` file. The code is documented to help you understand the logic behind the implementation.

```