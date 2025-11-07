# Numerical Letter Grade Converter

This software module provides a function to convert a list of GPAs into their corresponding letter grades based on a specified grading scale. It is designed to assist teachers in quickly determining letter grades from numerical GPAs.

## Main Functionality

The main function provided by this module is `numerical_letter_grade(grades)`, which takes a list of GPAs and returns a list of corresponding letter grades. The grading scale used is as follows:

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

This project does not require any external dependencies, so no additional installation steps are necessary beyond having Python installed on your system.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the directory where the project files are located.

   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can use the function in your Python scripts or run it directly in a Python environment.

   ```python
   from main import numerical_letter_grade

   # Example usage
   grades = [4.0, 3, 1.7, 2, 3.5]
   letter_grades = numerical_letter_grade(grades)
   print(letter_grades)  # Output: ['A+', 'B', 'C-', 'C', 'A-']
   ```

## Example

To see the function in action, you can run the following example:

```python
# Import the function
from main import numerical_letter_grade

# Define a list of GPAs
gpas = [4.0, 3.6, 2.8, 1.5, 0.0]

# Convert GPAs to letter grades
letter_grades = numerical_letter_grade(gpas)

# Print the results
print(letter_grades)  # Output: ['A+', 'A-', 'B', 'C-', 'E']
```

This example demonstrates how to convert a list of GPAs into letter grades using the provided function. You can modify the list of GPAs to test with different values.

## Conclusion

This module provides a simple and effective way to convert GPAs into letter grades using a predefined grading scale. It is easy to integrate into existing Python projects and requires no additional dependencies.