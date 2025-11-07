# Choose_Num User Manual

Welcome to the Choose_Num software! This application is designed to help you find the largest even integer within a specified range of two positive numbers. If no such number exists, the function will return -1. This manual will guide you through the installation process, introduce the main function, and provide instructions on how to use the software.

## Main Function

The core function of this software is `choose_num(x, y)`, which performs the following tasks:

- Takes two positive integers, `x` and `y`.
- Returns the largest even integer within the inclusive range `[x, y]`.
- If no even number exists within the range, it returns `-1`.

### Example Usage

- `choose_num(12, 15)` will return `14`.
- `choose_num(13, 12)` will return `-1`.

## Installation

This software does not require any external dependencies, making the installation process straightforward. You only need to have Python installed on your system.

### Step-by-Step Installation

1. **Ensure Python is Installed**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the code by cloning the repository or downloading it as a ZIP file.

3. **Navigate to the Project Directory**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

4. **Run the Code**: You can execute the code directly using Python. For example:
   ```bash
   python main.py
   ```

## How to Use

To use the `choose_num` function, follow these steps:

1. **Open a Python Environment**: You can use any Python environment, such as IDLE, Jupyter Notebook, or a simple Python script.

2. **Import the Function**: If you're using the function in a different script, make sure to import it:
   ```python
   from main import choose_num
   ```

3. **Call the Function**: Use the function by passing two positive integers as arguments:
   ```python
   result = choose_num(12, 15)
   print(result)  # Output will be 14
   ```

## Conclusion

The Choose_Num software is a simple yet effective tool for finding the largest even integer within a specified range. With no external dependencies, it is easy to install and use. We hope this manual helps you get started quickly and efficiently. If you have any questions or need further assistance, feel free to reach out to our support team.