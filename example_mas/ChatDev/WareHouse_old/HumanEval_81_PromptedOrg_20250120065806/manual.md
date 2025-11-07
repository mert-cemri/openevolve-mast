# Numerical Letter Grade Converter

This software module provides a function to convert a list of GPAs into their corresponding letter grades based on a predefined grading scale. It is designed to assist teachers in quickly determining letter grades from numerical GPAs.

## Main Functionality

The core functionality of this software is encapsulated in the `numerical_letter_grade` function. This function takes a list of GPAs as input and returns a list of corresponding letter grades based on the following grading scale:

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

This project does not require any external dependencies, making it simple and straightforward to use. You only need Python installed on your system.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

To use the `numerical_letter_grade` function, follow these steps:

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the function by importing it into your Python script or by directly running the `main.py` file. Here is an example of how to use it:

```python
from main import numerical_letter_grade

# Example usage
grades = [4.0, 3, 1.7, 2, 3.5]
letter_grades = numerical_letter_grade(grades)
print(letter_grades)  # Output: ['A+', 'B', 'C-', 'C', 'A-']
```

4. **Modify as Needed**: You can modify the list of GPAs to suit your needs and rerun the script to get the corresponding letter grades.

## Documentation

For further details on how to use the function and examples, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the grading conversion process.

This software is designed to be simple and efficient, providing quick conversion from numerical GPAs to letter grades without any additional setup or configuration.