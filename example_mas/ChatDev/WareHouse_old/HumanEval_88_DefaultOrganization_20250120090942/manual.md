# Sort Array Software

This software provides a function to sort an array of non-negative integers based on specific criteria. The array is sorted in ascending order if the sum of the first and last elements is odd, and in descending order if the sum is even.

## Main Functionality

The main function provided by this software is `sort_array(array)`, which takes an array of non-negative integers as input and returns a sorted copy of the array based on the following rules:

- If the sum of the first and last elements of the array is odd, the array is sorted in ascending order.
- If the sum is even, the array is sorted in descending order.
- The original array is not modified.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

### Environment Setup

This software does not require any external dependencies, making it easy to set up and use. You only need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository:**
   - Clone the repository or download the source code files to your local machine.

3. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the source code is located.

## Usage

To use the `sort_array` function, follow these steps:

1. **Open a Python Environment:**
   - You can use any Python environment, such as a terminal, command prompt, or an IDE like PyCharm or VSCode.

2. **Import the Function:**
   - Import the `sort_array` function from the `main.py` file.

   ```python
   from main import sort_array
   ```

3. **Call the