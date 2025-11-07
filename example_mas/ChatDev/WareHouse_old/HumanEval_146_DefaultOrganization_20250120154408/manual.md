manual.md

```
# SpecialFilter

A Python function to filter numbers based on specific criteria.

## Overview

The `specialFilter` function is designed to take an array of numbers as input and return the count of numbers that meet the following criteria:
- The number is greater than 10.
- Both the first and last digits of the number are odd (1, 3, 5, 7, 9).

### Example Usage

- `specialFilter([15, -73, 14, -15])` returns `1`.
- `specialFilter([33, -2, -3, 45, 21, 109])` returns `2`.

## Installation

This project does not require any external dependencies. You only need Python installed on your system to run the function.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository:**
   - Clone the repository to your local machine using the following command:
     ```
     git clone <repository-url>
     ```
   - Navigate to the project directory:
     ```
     cd <project-directory>
     ```

2. **Run the Function:**
   - Open the `main.py` file in your preferred Python editor or IDE.
   - Call the `specialFilter` function with your desired list of numbers.
   - Example:
     ```python
     result = specialFilter([15, -73, 14, -15])
     print(result)  # Output: 1
     ```

3. **Testing:**
   - You can test the function with different arrays to see how it filters numbers based on the specified criteria.

## Documentation

The function is self-contained and does not require additional documentation. The logic is implemented within the `main.py` file, which includes:
- A helper function `is_odd_digit` to check if a digit is odd.
- A helper function `first_and_last_digits_are_odd` to check if both the first and last digits of a number are odd.
- The main `specialFilter` function that iterates through the list and applies the filtering criteria.

For any further questions or support, please contact the development team.

```