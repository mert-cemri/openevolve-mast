# Search Function User Manual

## Introduction

This software provides a Python function named `search` that is designed to find the greatest integer in a list of positive integers. The integer must have a frequency in the list that is greater than or equal to the integer itself. If no such integer exists, the function will return -1.

## Main Function

### `search(lst)`

- **Description**: 
  - This function takes a non-empty list of positive integers as input and returns the greatest integer that meets the specified frequency condition.
  
- **Parameters**:
  - `lst`: A list of positive integers.

- **Returns**:
  - The greatest integer that has a frequency greater than or equal to the integer itself.
  - Returns `-1` if no such integer exists.

- **Examples**:
  ```python
  search([4, 1, 2, 2, 3, 1])  # Returns 2
  search([1, 2, 2, 3, 3, 3, 4, 4, 4])  # Returns 3
  search([5, 5, 4, 4, 4])  # Returns -1
  ```

## Installation

### Environment Setup

To use the `search` function, you need to have Python installed on your system. The function requires Python version 3.6 or higher.

1. **Install Python**: If you haven't already, download and install Python from the [official website](https://www.python.org/downloads/).

2. **Create a Virtual Environment** (optional but recommended):
   - Open your terminal or command prompt.
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
   - Ensure you have `pip` installed and run the following command to install the necessary dependencies:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

1. **Import the Function**:
   - Ensure that the `search` function is in your working directory or properly installed as a module.

2. **Call the Function**:
   - Use the `search` function by passing a list of positive integers as an argument.
   - Example:
     ```python
     from main import search

     result = search([4, 1, 2, 2, 3, 1])
     print(result)  # Output: 2
     ```

## Conclusion

This software provides a simple yet powerful function to analyze lists of integers based on their frequency. By following the installation and usage instructions, you can easily integrate this function into your Python projects. If you encounter any issues or have further questions, please refer to the documentation or contact support for assistance.