manual.md

```
# GPA to Letter Grade Converter

This software provides a simple function to convert a list of GPAs into their corresponding letter grades based on a specified grading scale. It is designed to assist educators in quickly determining letter grades from numerical GPAs.

## Main Function

The main function provided by this software is `numerical_letter_grade(grades)`, which takes a list of GPAs and returns a list of corresponding letter grades.

### Function Details

- **Function Name:** `numerical_letter_grade`
- **Parameters:** 
  - `grades` (list of float): A list of GPAs.
- **Returns:** 
  - list of str: A list of letter grades corresponding to the GPAs.

### Grading Scale

The function uses the following grading scale to convert GPAs to letter grades:

- GPA 4.0: A+
- GPA > 3.7: A
- GPA > 3.3: A-
- GPA > 3.0: B+
- GPA > 2.7: B
- GPA > 2.3: B-
- GPA > 2.0: C+
- GPA > 1.7: C
- GPA > 1.3: C-
- GPA > 1.0: D+
- GPA > 0.7: D
- GPA > 0.0: D-
- GPA 0.0: E

## Installation

This project does not require any external dependencies, making it straightforward to set up and use.

### Quick Install

Since there are no external dependencies, you can directly use the provided Python script. Ensure you have Python installed on your system.

## Usage

1. **Clone the Repository:**
   - Download or clone the repository to your local machine.

2. **Navigate to the Project Directory:**
   - Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Function:**
   - You can use the function in a Python script or an interactive Python session. Here is an example of how to use it:

```python
from main import numerical_letter_grade

# Example usage
gpas = [4.0, 3.0, 1.7, 2.0, 3.5]
letter_grades = numerical_letter_grade(gpas)
print(letter_grades)  # Output: ['A+', 'B', 'C-', 'C', 'A-']
```

## Documentation

For further details on how the function works, please refer to the comments within the `main.py` file. The function is well-documented to help you understand its usage and the grading logic.

Feel free to modify the code to suit your specific needs or grading criteria.
```
