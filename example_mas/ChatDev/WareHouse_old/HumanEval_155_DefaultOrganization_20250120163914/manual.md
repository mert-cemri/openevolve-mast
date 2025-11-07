# Even Odd Count Software

This software provides a simple function to count the number of even and odd digits in a given integer. It is designed to be straightforward and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this software is encapsulated in the `even_odd_count` function. This function takes an integer as input and returns a tuple containing two values: the count of even digits and the count of odd digits in the integer.

### Example Usage

- `even_odd_count(-12)` returns `(1, 1)`, indicating there is 1 even digit and 1 odd digit.
- `even_odd_count(123)` returns `(1, 2)`, indicating there is 1 even digit and 2 odd digits.

## Installation

Since this project does not require any external dependencies, setting up the environment is straightforward. You only need to have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

## How to Use

1. **Open the main.py file**: This file contains the `even_odd_count` function.

2. **Call the function**: You can call the `even_odd_count` function with any integer to get the count of even and odd digits. For example:
   ```python
   result = even_odd_count(12345)
   print(result)  # Output will be (2, 3)
   ```

3. **Run the script**: Execute the script using Python to see the results.
   ```bash
   python main.py
   ```

## Documentation

The `even_odd_count` function is documented within the code itself. The function is designed to handle both positive and negative integers, converting them to their absolute values before processing. This ensures that the sign of the number does not affect the digit count.

For further information or support, please contact the development team.