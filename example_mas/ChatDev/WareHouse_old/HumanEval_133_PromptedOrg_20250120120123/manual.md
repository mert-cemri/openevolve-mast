# Sum Squares User Manual

Welcome to the Sum Squares software! This application provides a simple function to compute the sum of squares of the ceiling values of a list of numbers. This document will guide you through the installation process, introduce the main function, and provide instructions on how to use the software.

## Main Function

The primary function of this software is `sum_squares(lst)`. This function takes a list of numbers as input and returns the sum of the squares of each number after rounding them up to the nearest integer (ceiling).

### Function Details

- **Function Name:** `sum_squares`
- **Input:** A list of numbers (e.g., `[1.4, 4.2, 0]`)
- **Output:** An integer representing the sum of the squares of the ceiling values of the input list (e.g., `29` for the input `[1.4, 4.2, 0]`).

### Example Usage

- For `lst = [1, 2, 3]`, the output will be `14`.
- For `lst = [1, 4, 9]`, the output will be `98`.
- For `lst = [1, 3, 5, 7]`, the output will be `84`.
- For `lst = [1.4, 4.2, 0]`, the output will be `29`.
- For `lst = [-2.4, 1, 1]`, the output will be `6`.

## Installation

This software does not require any external dependencies beyond Python itself. You can run the software on any system with Python installed.

### Step-by-Step Installation

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository:**
   - Clone the repository using Git or download the source code as a ZIP file and extract it.

3. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the source code is located.

4. **Run the Code:**
   - You can run the code directly using Python. No additional setup is required.

## How to Use

1. **Open a Python Environment:**
   - You can use any Python environment, such as IDLE, PyCharm, or a terminal.

2. **Import the Function:**
   - Navigate to the directory containing `main.py` and import the `sum_squares` function.

   ```python
   from main import sum_squares
   ```

3. **Call the Function:**
   - Pass a list of numbers to the `sum_squares` function and print the result.

   ```python
   result = sum_squares([1.4, 4.2, 0])
   print(result)  # Output: 29
   ```

## Conclusion

This software provides a straightforward way to calculate the sum of squares of ceiling values from a list of numbers. With no external dependencies, it is easy to set up and use. If you have any questions or need further assistance, please feel free to reach out to our support team.