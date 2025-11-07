```markdown
# SpecialFilter

A Python function to filter numbers based on specific criteria.

## Introduction

The `specialFilter` function is designed to process an array of numbers and return the count of numbers that meet the following criteria:
- The number is greater than 10.
- Both the first and last digits of the number are odd (1, 3, 5, 7, 9).

This function can be useful in scenarios where you need to filter and analyze datasets based on specific numeric properties.

## Quick Install

No external dependencies are required for this project, so you can directly use the function in your Python environment without any additional installations.

## How to Use

1. **Clone or Download the Repository**

   You can clone the repository using Git or download the ZIP file and extract it to your desired location.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

   ```bash
   cd path/to/project-directory
   ```

3. **Run the Function**

   You can use the `specialFilter` function by importing it into your Python script or interactive session. Here's an example of how to use it:

   ```python
   from main import specialFilter

   # Example usage
   result1 = specialFilter([15, -73, 14, -15])
   print(result1)  # Output: 1

   result2 = specialFilter([33, -2, -3, 45, 21, 109])
   print(result2)  # Output: 2
   ```

## Function Explanation

- **Function Name:** `specialFilter`
- **Parameters:** 
  - `nums`: A list of integers.
- **Returns:** An integer representing the count of numbers that satisfy the criteria.

### Criteria for Filtering

1. **Greater than 10:** The number must be greater than 10.
2. **Odd First and Last Digits:** The first and last digits of the number must be odd. This is checked by converting the number to a string and examining the first and last characters.

### Example

For the input `[15, -73, 14, -15]`, the function returns `1` because only `15` meets the criteria (greater than 10, first digit `1` and last digit `5` are both odd).

For the input `[33, -2, -3, 45, 21, 109]`, the function returns `2` because `33` and `109` meet the criteria.

## Conclusion

The `specialFilter` function is a simple yet effective tool for filtering numbers based on specific digit properties. It can be easily integrated into larger projects or used for data analysis tasks where such filtering is required.
```
