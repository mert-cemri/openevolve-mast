manual.md

```
# GPA to Letter Grade Converter

This software module provides a function to convert a list of GPAs (Grade Point Averages) into their corresponding letter grades based on a specified grading scale. This can be particularly useful for educators or institutions that need to convert numerical GPAs into letter grades for reporting purposes.

## Main Functionality

The main function provided by this module is `numerical_letter_grade(grades)`, which takes a list of GPAs as input and returns a list of corresponding letter grades.

### Function: numerical_letter_grade

- **Input**: A list of GPAs (floats).
- **Output**: A list of letter grades (strings) corresponding to the input GPAs.

#### Grading Scale

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

### Example Usage

```python
# Example usage of the numerical_letter_grade function
grades = [4.0, 3, 1.7, 2, 3.5]
letter_grades = numerical_letter_grade(grades)
print(letter_grades)  # Output: ['A+', 'B', 'C-', 'C', 'A-']
```

## Installation

This module does not have any external dependencies, so no additional installation steps are required beyond having Python installed on your system.

### Prerequisites

- Python 3.x

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Script**: You can run the script using Python to see the conversion in action.

   ```bash
   python main.py
   ```

4. **Modify the Input**: You can modify the list of GPAs in the script to test with different values.

## Additional Information

This module is designed to be simple and straightforward, focusing solely on converting GPAs to letter grades. It does not include any graphical user interface or additional features beyond the core functionality.

For any questions or support, please contact our support team at support@chatdev.com.

```