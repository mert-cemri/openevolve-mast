# SpecialFilter User Manual

Welcome to the SpecialFilter software! This tool is designed to filter numbers based on specific criteria. It helps you identify numbers in an array that are greater than 10 and have both their first and last digits as odd numbers (1, 3, 5, 7, 9).

## Main Functionality

The main functionality of the SpecialFilter software is encapsulated in the `specialFilter` function. This function takes an array of numbers as input and returns the count of numbers that meet the specified criteria.

### Function: `specialFilter(nums)`

- **Input**: An array of numbers (e.g., `[15, -73, 14, -15]`).
- **Output**: An integer representing the number of elements in the array that are greater than 10 and have both the first and last digits as odd numbers.

#### Example Usage

```python
result = specialFilter([15, -73, 14, -15])
print(result)  # Output: 1

result = specialFilter([33, -2, -3, 45, 21, 109])
print(result)  # Output: 2
```

## Installation

The SpecialFilter software is implemented in Python and does not require any external dependencies. You can run it in any standard Python environment.

### Quick Install

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: Clone or download the source code to your local machine.

3. **Run the code**: Navigate to the directory containing the `main.py` file and execute it using Python.

```bash
python main.py
```

## How to Use

1. **Prepare your data**: Create an array of numbers that you want to filter.

2. **Call the `specialFilter` function**: Pass your array to the `specialFilter` function to get the count of numbers that meet the criteria.

3. **Interpret the result**: The function will return an integer indicating how many numbers in your array are greater than 10 and have both the first and last digits as odd numbers.

## Documentation

For further details on how the function works, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the function.

If you encounter any issues or have questions, feel free to reach out for support. We hope you find the SpecialFilter software useful for your number filtering needs!