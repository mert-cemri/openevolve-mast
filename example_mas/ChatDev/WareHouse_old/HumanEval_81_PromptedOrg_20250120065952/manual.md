# Numerical Letter Grade Converter

This software module provides a function to convert a list of GPAs (Grade Point Averages) into corresponding letter grades based on a specified grading scale. This can be particularly useful for educators or institutions that need to translate numerical GPAs into letter grades for reporting purposes.

## Main Function

### `numerical_letter_grade(grades)`

- **Description**: Converts a list of GPAs to a list of letter grades.
- **Arguments**: 
  - `grades` (list of float): A list containing GPAs.
- **Returns**: 
  - `list of str`: A list of corresponding letter grades.

### Grading Scale

The conversion from GPA to letter grade is based on the following scale:

- 4.0 -> A+
- > 3.7 -> A
- > 3.3 -> A-
- > 3.0 -> B+
- > 2.7 -> B
- > 2.3 -> B-
- > 2.0 -> C+
- > 1.7 -> C
- > 1.3 -> C-
- > 1.0 -> D+
- > 0.7 -> D
- > 0.0 -> D-
- 0.0 -> E

## Installation

This module does not require any external dependencies, making it easy to integrate into existing Python projects.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python environment. Simply copy the code into your project or import the module if it's part of a larger codebase.

## How to Use

1. **Copy the Code**: Ensure the function `numerical_letter_grade` is included in your Python script or module.

2. **Call the Function**: Pass a list of GPAs to the function to receive a list of letter grades.

   ```python
   grades = [4.0, 3, 1.7, 2, 3.5]
   letter_grades = numerical_letter_grade(grades)
   print(letter_grades)  # Output: ['A+', 'B', 'C-', 'C', 'A-']
   ```

3. **Integrate into Larger Systems**: This function can be integrated into larger educational software systems where GPA to letter grade conversion is necessary.

## Documentation

For further details on using this module, please refer to the inline comments within the code. The function is designed to be straightforward and easy to understand, with a clear mapping of GPAs to letter grades.

This module is a simple yet effective tool for educators and institutions looking to automate the conversion of GPAs to letter grades.