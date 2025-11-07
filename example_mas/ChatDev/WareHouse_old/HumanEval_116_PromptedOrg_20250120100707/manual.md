# Sort Array User Manual

Welcome to the Sort Array software! This tool is designed to sort an array of integers based on specific criteria. This manual will guide you through the main functions of the software, how to install the necessary environment dependencies, and how to use the software effectively.

## Main Functions

The primary function of this software is to sort an array of integers according to the following rules:

1. **Non-negative Integers**: These are sorted based on the number of ones in their binary representation in ascending order. If two numbers have the same number of ones, they are further sorted by their decimal value.

2. **Negative Integers**: These are sorted in ascending order based on their decimal value.

The function `sort_array(arr)` takes an array of integers as input and returns a new array sorted according to the rules mentioned above.

### Example Usage

- `sort_array([1, 5, 2, 3, 4])` will return `[1, 2, 3, 4, 5]`
- `sort_array([-2, -3, -4, -5, -6])` will return `[-6, -5, -4, -3, -2]`
- `sort_array([1, 0, 2, 3, 4])` will return `[0, 1, 2, 3, 4]`

## Installation

To use the Sort Array software, you need to have Python installed on your system. The software does not require any additional dependencies beyond the standard Python library.

### Quick Install

1. **Ensure Python is installed**: You can download Python from the official website [here](https://www.python.org/downloads/).

2. **Clone the repository**: If you have access to the source code repository, clone it to your local machine.

3. **Navigate to the project directory**: Use the command line to navigate to the directory where the `main.py` file is located.

## How to Use

1. **Open the `main.py` file**: You can use any text editor or IDE of your choice.

2. **Modify the input array**: In the `sort_array(arr)` function, replace `arr` with the array you wish to sort.

3. **Run the script**: Execute the script using Python. You can do this by running the command `python main.py` in your command line or terminal.

4. **View the output**: The sorted array will be printed to the console.

## Documentation

For further information on how the sorting algorithm works or to contribute to the project, please refer to the comments within the `main.py` file. The code is documented to help you understand the logic behind the sorting process.

Thank you for using the Sort Array software! If you have any questions or need further assistance, please feel free to reach out.