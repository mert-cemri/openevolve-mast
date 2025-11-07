# Search Function User Manual

## Introduction

This software provides a function named `search` that processes a non-empty list of positive integers. The function identifies and returns the greatest integer that is greater than zero and has a frequency in the list that is greater than or equal to the integer itself. If no such integer exists, the function returns -1.

### Main Functionality

- **Function Name:** `search`
- **Input:** A list of positive integers.
- **Output:** The greatest integer meeting the specified frequency condition, or -1 if no such integer exists.

### Examples

- `search([4, 1, 2, 2, 3, 1])` returns `2`
- `search([1, 2, 2, 3, 3, 3, 4, 4, 4])` returns `3`
- `search([5, 5, 4, 4, 4])` returns `-1`

## Installation

### Prerequisites

- Python 3.x installed on your system.

### Installation Steps

1. **Clone the Repository:**
   Clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Project Directory:**
   Open a terminal and navigate to the directory where `main.py` is located.

3. **Install Dependencies:**
   There are no additional dependencies required for this software, as it utilizes Python's standard library.

## Usage

1. **Open the Terminal:**
   Ensure you are in the directory containing the `main.py` file.

2. **Run the Python Script:**
   You can test the `search` function by executing the script in a Python environment. For example:

   ```python
   from main import search

   # Test the function with a sample list
   result = search([4, 1, 2, 2, 3, 1])
   print(result)  # Output should be 2
   ```

3. **Modify Input:**
   You can modify the input list to test different scenarios as needed.

## Documentation

For further details on how the function works, refer to the docstring provided in the `main.py` file. It includes a description of the function's purpose, input parameters, and expected output.

## Support

For any issues or questions regarding the usage of this software, please contact our support team at support@chatdev.com. We are here to assist you with any inquiries you may have.