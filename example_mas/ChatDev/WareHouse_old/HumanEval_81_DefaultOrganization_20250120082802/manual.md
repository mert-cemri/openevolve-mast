manual.md

```
# GPA to Letter Grade Converter

This software provides a simple function to convert a list of GPAs (Grade Point Averages) into their corresponding letter grades based on a specified grading scale. It is designed to assist teachers in quickly determining letter grades for students based on their GPAs.

## Main Functionality

The main function provided by this software is `numerical_letter_grade(grades)`. This function takes a list of GPAs as input and returns a list of corresponding letter grades. The grading scale used is as follows:

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

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the code by either cloning the repository or downloading it as a ZIP file and extracting it to your desired location.

3. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the code is located.

## Usage

To use the `numerical_letter_grade` function, follow these steps:

1. **Open the main.py File**: Open the `main.py` file in a text editor or an integrated development environment (IDE).

2. **Call the Function**: Use the function by passing a list of GPAs as an argument. For example:

   ```python
   print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))
   ```

   This will output: `['A+', 'B', 'C-', 'C', 'A-']`

3. **Run the Script**: Execute the script by running the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

   This will display the letter grades corresponding to the GPAs provided.

## Conclusion

This software provides a straightforward and efficient way to convert GPAs to letter grades, making it a useful tool for educators. With no external dependencies, it is easy to set up and use. Simply follow the instructions above to get started.

```