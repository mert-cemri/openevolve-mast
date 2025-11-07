# Can Arrange Function

This software provides a Python function `can_arrange` that determines the largest index of an element in an array that is not greater than or equal to the element immediately preceding it. If no such element exists, the function returns -1. This function is useful for analyzing sequences of numbers to identify points of non-increasing order.

## Main Functionality

- **Function Name:** `can_arrange`
- **Purpose:** To find the largest index of an element in an array that is not greater than or equal to the element immediately preceding it.
- **Input:** A list of integers with no duplicate values.
- **Output:** An integer representing the largest index of a non-increasing element, or -1 if the array is strictly increasing.

### Examples

- `can_arrange([1, 2, 4, 3, 5])` returns `3`
- `can_arrange([1, 2, 3])` returns `-1`

## Installation

To use the `can_arrange` function, you need to have Python installed on your system. The function does not require any additional libraries or dependencies.

### Steps to Install Python

1. **Download Python:**
   - Visit the official Python website: [python.org](https://www.python.org/)
   - Download the latest version of Python for your operating system.

2. **Install Python:**
   - Follow the installation instructions provided on the Python website for your specific operating system.

3. **Verify Installation:**
   - Open a terminal or command prompt.
   - Type `python --version` and press Enter.
   - Ensure that the installed version of Python is displayed.

## Usage

1. **Create a Python File:**
   - Open a text editor or an Integrated Development Environment (IDE).
   - Create a new file named `main.py`.

2. **Copy the Function Code:**
   - Copy the following code into `main.py`:

   ```python
   def can_arrange(arr):
       largest_index = -1
       for i in range(1, len(arr)):
           if arr[i] < arr[i - 1]:
               largest_index = i
       return largest_index

   # Example usage:
   # print(can_arrange([1, 2, 4, 3, 5]))  # Output: 3
   # print(can_arrange([1, 2, 3]))        # Output: -1
   ```

3. **Run the Code:**
   - Save the `main.py` file.
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the script by typing `python main.py` and pressing Enter.

4. **Test the Function:**
   - Uncomment the example usage lines in `main.py` to test the function with sample inputs.
   - Modify the input arrays as needed to test different scenarios.

## Conclusion

The `can_arrange` function is a simple yet effective tool for analyzing sequences of numbers. By following the installation and usage instructions, you can easily integrate this function into your Python projects. If you have any questions or need further assistance, please feel free to reach out.