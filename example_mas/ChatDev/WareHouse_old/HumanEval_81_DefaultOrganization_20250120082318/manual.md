# Numerical Letter Grade Converter

This software module provides a function to convert a list of GPAs into corresponding letter grades based on a specified grading scale. It is designed to assist teachers in converting numerical GPAs into letter grades efficiently.

## Main Functionality

The main function of this software is `numerical_letter_grade(grades)`, which takes a list of GPAs and returns a list of corresponding letter grades. The conversion is based on the following grading scale:

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

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Script**: You can run the script using Python to test the function.

```bash
python main.py
```

## How to Use

1. **Import the Function**: If you are integrating this function into another project, you can import it as follows:

    ```python
    from main import numerical_letter_grade
    ```

2. **Call the Function**: Pass a list of GPAs to the function to get the corresponding letter grades.

    ```python
    grades = [4.0, 3, 1.7, 2, 3.5]
    letter_grades = numerical_letter_grade(grades)
    print(letter_grades)  # Output: ['A+', 'B', 'C-', 'C', 'A-']
    ```

## Example Usage

Here is an example of how to use the `numerical_letter_grade` function:

```python
# Example usage:
grades = [4.0, 3, 1.7, 2, 3.5]
letter_grades = numerical_letter_grade(grades)
print(letter_grades)  # Output: ['A+', 'B', 'C-', 'C', 'A-']
```

This example demonstrates how to convert a list of GPAs into letter grades using the provided function.

## Documentation

For further details and documentation, please refer to the comments within the `main.py` file, which provide additional insights into the function's implementation and usage.