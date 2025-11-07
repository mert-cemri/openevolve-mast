# Numerical Letter Grade Converter

This software provides a function to convert numerical GPAs into letter grades based on a predefined grading scale. It is designed to assist teachers in quickly determining letter grades for students based on their GPA scores.

## Main Function

The main function of this software is `numerical_letter_grade(grades)`, which takes a list of GPAs as input and returns a list of corresponding letter grades.

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

### Example Usage

```python
grades = [4.0, 3, 1.7, 2, 3.5]
letter_grades = numerical_letter_grade(grades)
print(letter_grades)  # Output: ['A+', 'B', 'C-', 'C', 'A-']
```

## Installation

This software does not require any external dependencies. You can run it in any Python environment without additional installations.

## How to Use

1. **Prepare Your Environment**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Python File**: Copy the provided code into a Python file, for example, `main.py`.

3. **Run the Code**: Execute the Python file using a Python interpreter. You can do this by opening a terminal or command prompt, navigating to the directory containing your `main.py` file, and running the command:
   ```
   python main.py
   ```

4. **Input GPAs**: Modify the `grades` list in the code to include the GPAs you wish to convert to letter grades.

5. **View Results**: The program will output the corresponding letter grades for the input GPAs.

This software is a simple and efficient tool for converting GPAs to letter grades, making it ideal for educators and institutions looking to streamline their grading process.