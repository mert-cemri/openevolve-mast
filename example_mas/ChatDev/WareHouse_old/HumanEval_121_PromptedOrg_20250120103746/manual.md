# Solution User Manual

## Overview

This software provides a simple function to calculate the sum of odd elements located at even positions in a given list of integers. It is designed to be straightforward and efficient, requiring no external dependencies.

## Main Function

### `solution(lst)`

- **Description**: This function takes a non-empty list of integers and returns the sum of all odd elements that are located at even positions (0-based index) in the list.

- **Parameters**:
  - `lst` (list): A non-empty list of integers.

- **Returns**:
  - `int`: The sum of all odd elements at even positions in the list.

- **Examples**:
  - `solution([5, 8, 7, 1])` returns `12`
  - `solution([3, 3, 3, 3, 3])` returns `9`
  - `solution([30, 13, 24, 321])` returns `0`

## Installation

This software does not require any external libraries or dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Code**: You can run the code directly using Python. No additional installation steps are required.

## Usage

To use the `solution` function, follow these steps:

1. **Open a Python Environment**: You can use a Python IDE, a text editor with Python support, or a terminal.

2. **Import the Function**: If you are using a Python script, ensure that the `solution` function is accessible. You can do this by placing the `main.py` file in the same directory as your script or by importing it directly if it's part of a module.

3. **Call the Function**: Pass a list of integers to the `solution` function and capture the result.

   ```python
   from main import solution

   result = solution([5, 8, 7, 1])
   print(result)  # Output: 12
   ```

4. **View the Result**: The function will return the sum of odd elements at even positions, which you can print or use in further calculations.

## Conclusion

This software provides a simple yet effective solution for summing odd elements at even positions in a list. With no dependencies required, it is easy to integrate into any Python project. For any questions or support, please contact our development team.