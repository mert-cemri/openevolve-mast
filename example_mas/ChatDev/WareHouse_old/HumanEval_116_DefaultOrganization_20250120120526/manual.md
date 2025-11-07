# Sort Array User Manual

Welcome to the Sort Array software! This tool is designed to sort arrays of integers based on specific criteria involving their binary representation and decimal values. This manual will guide you through the main functions of the software, how to set up your environment, and how to use the software effectively.

## Main Functions

The primary function of this software is `sort_array`, which sorts an array of integers based on the following criteria:

1. **Non-negative Integers**: These are sorted by the number of ones in their binary representation in ascending order. If two numbers have the same number of ones, they are further sorted by their decimal value.

2. **Negative Integers**: These are sorted by their decimal value in ascending order.

### Example Usage

- `sort_array([1, 5, 2, 3, 4])` will return `[1, 2, 3, 4, 5]`.
- `sort_array([-2, -3, -4, -5, -6])` will return `[-6, -5, -4, -3, -2]`.
- `sort_array([1, 0, 2, 3, 4])` will return `[0, 1, 2, 3, 4]`.

## Installation

### Environment Setup

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Move into the directory where the project files are located.

   ```bash
   cd <project-directory>
   ```

4. **Run the Software**: You can run the software directly using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Input**: Provide an array of integers as input to the `sort_array` function.

2. **Execution**: The function will process the array and return a new array sorted according to the specified criteria.

3. **Output**: The sorted array will be printed to the console if you run the example usage provided in the `main.py` file.

## Documentation

For further details on the implementation and to view the source code, please refer to the `main.py` file in the project directory. The code is well-commented to help you understand the logic behind the sorting algorithm.

## Support

If you encounter any issues or have questions about using the Sort Array software, please feel free to reach out to our support team or consult the documentation provided within the code.

Thank you for choosing our software to assist with your array sorting needs!