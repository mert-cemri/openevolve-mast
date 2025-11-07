manual.md

```
# Solution Function

This software provides a simple Python function to solve a specific problem: given a non-empty list of integers, it returns the sum of all odd elements that are in even positions (0-based index) in the list.

## Main Functionality

The main function of this software is:

- **solution(lst):** This function takes a list of integers as input and returns the sum of all odd integers that are located at even indices in the list.

### Examples

- `solution([5, 8, 7, 1])` returns `12`
- `solution([3, 3, 3, 3, 3])` returns `9`
- `solution([30, 13, 24, 321])` returns `0`

## Installation

This software does not require any external dependencies, making it easy to set up and use. You simply need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Clone or Download the Repository:**
   - You can clone the repository using Git or download the ZIP file and extract it to your desired location.

3. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

## Usage

To use the solution function, follow these steps:

1. **Open a Terminal or Command Prompt:**
   - Navigate to the directory where the `main.py` file is located.

2. **Run Python Interactive Shell or Script:**
   - You can test the function directly in the Python interactive shell or by writing a script.

3. **Example Usage:**

   ```python
   from main import solution

   # Example list
   lst = [5, 8, 7, 1]

   # Call the solution function
   result = solution(lst)

   # Print the result
   print(result)  # Output: 12
   ```

4. **Modify the Input List:**
   - You can modify the input list `lst` to test with different sets of integers.

## Conclusion

This software provides a straightforward solution to sum odd integers at even indices in a list. With no external dependencies, it is easy to set up and use. Simply modify the input list to suit your needs and call the `solution` function to get the desired result.
```