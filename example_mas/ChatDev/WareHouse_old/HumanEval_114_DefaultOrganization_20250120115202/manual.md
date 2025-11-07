# minSubArraySum User Manual

## Introduction

The `minSubArraySum` function is a Python-based utility designed to find the minimum sum of any non-empty sub-array from a given list of integers. This function is particularly useful for tasks that require analysis of sub-array sums, such as in financial data analysis or algorithmic challenges.

## Main Functionality

- **Function Name**: `minSubArraySum`
- **Purpose**: To compute the minimum sum of any non-empty sub-array within a list of integers.
- **Input**: A list of integers, `nums`.
- **Output**: An integer representing the minimum sum of any non-empty sub-array.

### Example Usage

```python
# Example 1
result = minSubArraySum([2, 3, 4, 1, 2, 4])
print(result)  # Output: 1

# Example 2
result = minSubArraySum([-1, -2, -3])
print(result)  # Output: -6
```

## Installation

This project does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Step-by-Step Installation Guide

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted on a version control system like GitHub, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: 

   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can execute the `main.py` file directly using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Prepare Your Input**: Ensure your input is a list of integers. The function does not handle non-integer inputs or empty lists.

2. **Call the Function**: Use the `minSubArraySum` function with your list as the argument.

3. **Interpret the Output**: The function will return the minimum sum of any non-empty sub-array.

## Additional Information

- **Edge Cases**: The function is designed to handle lists with both positive and negative integers. It assumes the list is non-empty as per the problem statement.

- **Performance**: The function efficiently computes the result in linear time, O(n), where n is the number of elements in the list.

## Support

For further assistance or to report issues, please contact the development team at [support@chatdev.com](mailto:support@chatdev.com).

---

This manual provides all necessary information to effectively use the `minSubArraySum` function. Ensure to follow the installation and usage instructions for optimal performance.