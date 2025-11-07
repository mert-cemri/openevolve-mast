# Numerical Letter Grade Converter

This software module provides a function to convert a list of GPAs into their corresponding letter grades based on a specified grading scale. It is designed to assist teachers in grading students by automating the conversion of numerical GPAs to letter grades.

## Main Function

### `numerical_letter_grade(grades)`

- **Purpose**: Converts a list of GPAs to their corresponding letter grades.
- **Parameters**: 
  - `grades` (list of float): A list of GPAs.
- **Returns**: 
  - `list of str`: A list of letter grades corresponding to the GPAs.

### Grading Scale

The conversion is based on the following grading scale:

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

There are no external dependencies required for this project. You can simply download the `main.py` file and run it in your Python environment.

## Usage

1. **Download the Code**: Ensure you have the `main.py` file in your working directory.

2. **Run the Function**: You can use the function `numerical_letter_grade` by importing it into your Python script or interactive session.

   Example:
   ```python
   from main import numerical_letter_grade

   grades = [4.0, 3, 1.7, 2, 3.5]
   letter_grades = numerical_letter_grade(grades)
   print(letter_grades)  # Output: ['A+', 'B', 'C-', 'C', 'A-']
   ```

3. **Interpret the Results**: The function will return a list of letter grades corresponding to the input GPAs.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The code is straightforward and well-documented to assist you in understanding the logic and usage.

## Support

If you encounter any issues or have questions about using this software, please contact our support team for assistance. We are here to help you make the most out of this tool.