# Search Function User Manual

## Introduction

The `search` function is a Python utility designed to process a list of positive integers and identify the greatest integer that meets specific frequency criteria. Specifically, it returns the greatest integer whose frequency in the list is greater than or equal to the integer itself. If no such integer exists, the function returns -1.

## Main Functionality

- **Function Name**: `search`
- **Purpose**: To find the greatest integer in a list that has a frequency greater than or equal to its value.
- **Input**: A non-empty list of positive integers.
- **Output**: The greatest integer meeting the criteria, or -1 if no such integer exists.

### Examples

- `search([4, 1, 2, 2, 3, 1])` returns `2`
- `search([1, 2, 2, 3, 3, 3, 4, 4, 4])` returns `3`
- `search([5, 5, 4, 4, 4])` returns `-1`

## Installation

### Environment Setup

This function does not require any external dependencies beyond the Python Standard Library. Ensure you have Python installed on your system.

### Installation Steps

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Move into the directory containing the `main.py` file.
   ```bash
   cd <directory-name>
   ```

3. **Run the Function**: You can execute the function directly in a Python environment or script.

## Usage

To use the `search` function, follow these steps:

1. **Import the Function**: If the function is in a module, import it into your script or interactive session.
   ```python
   from main import search
   ```

2. **Call the Function**: Pass a list of positive integers to the function.
   ```python
   result = search([4, 1, 2, 2, 3, 1])
   print(result)  # Output will be 2
   ```

3. **Interpret the Result**: The function will return the greatest integer that meets the criteria or -1 if no such integer exists.

## Additional Information

- **Python Version**: Ensure you are using Python 3.x to avoid compatibility issues.
- **No External Libraries**: The function uses Python's built-in `collections.Counter` for counting frequencies, so no additional libraries are needed.

## Troubleshooting

- **Incorrect Output**: Ensure the input list contains only positive integers.
- **Error Messages**: Check for syntax errors or incorrect import statements if the function does not execute.

This user manual provides all necessary information to effectively utilize the `search` function in your Python projects. If further assistance is needed, consider reaching out to the development team or consulting Python documentation for additional support.