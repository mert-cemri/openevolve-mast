```markdown
# Parse Nested Parentheses

A Python utility to determine the deepest level of nesting for groups of parentheses in a given string.

## Overview

The `parse_nested_parens` function is designed to analyze a string containing multiple groups of nested parentheses, separated by spaces. For each group, it calculates and returns the deepest level of nesting.

### Example

For the input string `'(()()) ((())) () ((())()())'`, the function will return `[2, 3, 1, 3]`, indicating the maximum nesting levels for each group.

## Installation

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd <project-directory>
   ```

3. **Install Python**

   Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

4. **Set Up Virtual Environment (Optional but Recommended)**

   Create a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**

   There are no external dependencies required for this project. However, if you plan to extend the functionality, you can manage dependencies using a `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the `parse_nested_parens` function, follow these steps:

1. **Open the `main.py` File**

   The function is implemented in the `main.py` file. You can directly call the function from this file or import it into another Python script.

2. **Call the Function**

   Pass a string of nested parentheses to the function and capture the output:

   ```python
   from main import parse_nested_parens

   result = parse_nested_parens('(()()) ((())) () ((())()())')
   print(result)  # Output: [2, 3, 1, 3]
   ```

3. **Run the Script**

   Execute the script to see the results:

   ```bash
   python main.py
   ```

## Documentation

For further documentation and examples, refer to the docstring within the `main.py` file. The function is well-documented to help you understand its usage and expected input/output.

## Support

For any issues or questions, please contact the development team at [support@chatdev.com](mailto:support@chatdev.com).

```
