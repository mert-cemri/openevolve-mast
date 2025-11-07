# Numerical Letter Grade Converter

This software module provides a function to convert a list of GPAs (Grade Point Averages) into their corresponding letter grades based on a specified grading scale. It is designed to assist educators in quickly determining letter grades from numerical GPAs.

## Main Functionality

The main function provided by this software is `numerical_letter_grade(grades)`. This function takes a list of GPAs as input and returns a list of corresponding letter grades based on the following grading scale:

- 4.0: A+
- > 3.7: A
- > 3.3: A-
- > 3.0: B+
- > 2.7: B
- > 2.3: B-
- > 2.0: C+
- > 1.7: C
- > 1.3: C-
- > 1.0: D+
- > 0.7: D
- > 0.0: D-
- 0.0: E

### Example Usage

```python
# Example usage of the numerical_letter_grade function
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # Output: ['A+', 'B', 'C-', 'C', 'A-']
```

## Installation

This project does not require any external dependencies, making it simple to set up and use. You only need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the code by cloning the repository or downloading the ZIP file.

3. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the code is located.

## How to Use

1. **Open the Code File**: Open `main.py` in your preferred code editor.

2. **Run the Code**: You can run the code directly in your terminal or command prompt by navigating to the directory containing `main.py` and executing the following command:

   ```bash
   python main.py
   ```

3. **Modify Input as Needed**: You can modify the list of GPAs in the `numerical_letter_grade` function call to test with different values.

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is well-documented with inline comments explaining its purpose and usage.

This software is designed to be straightforward and easy to integrate into larger systems if needed. Feel free to modify and adapt it to suit your specific grading needs.