# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a given string. It is designed to handle strings containing multiple groups of nested parentheses, ensuring that each group is properly balanced and not nested within each other.

## Main Functionality

### `separate_paren_groups`

- **Purpose**: To separate groups of balanced parentheses from a given string and return them as a list of strings.
- **Input**: A string containing multiple groups of nested parentheses. Spaces in the input string are ignored.
- **Output**: A list of strings, each representing a separate group of balanced parentheses.

#### Example Usage

```python
from main import separate_paren_groups

result = separate_paren_groups('( ) (( )) (( )( ))')
print(result)  # Output: ['()', '(())', '(()())']
```

## Installation

This software does not require any external dependencies. It is implemented in Python and requires Python version 3.6 or higher.

### Setting Up the Environment

1. **Ensure Python is Installed**: Make sure you have Python 3.6 or higher installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change into the project directory:
   ```bash
   cd <project-directory>
   ```

4. **Install Python Dependencies**: Although there are no external dependencies, you can create a virtual environment to manage your Python packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

5. **Run the Code**: You can execute the code using a Python interpreter:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: Import the `separate_paren_groups` function from the `main.py` file.

2. **Call the Function**: Pass a string containing groups of parentheses to the function. The function will return a list of strings, each representing a separate group of balanced parentheses.

3. **Handle the Output**: Use the returned list as needed in your application.

## Additional Information

- **No GUI**: This software is designed to be used as a backend utility and does not include any graphical user interface components.
- **No External Libraries**: The software is lightweight and does not rely on any external Python libraries, making it easy to integrate into other projects.

For any further questions or support, please contact our development team.