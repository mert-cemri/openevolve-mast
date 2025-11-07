# Total Match Function

This software provides a simple Python function, `total_match`, which compares two lists of strings and returns the list with the fewer total number of characters. If both lists have the same number of characters, it returns the first list.

## Main Functionality

### `total_match(lst1, lst2)`

- **Purpose**: To compare two lists of strings and return the list with fewer total characters.
- **Parameters**:
  - `lst1`: A list of strings.
  - `lst2`: A list of strings.
- **Returns**: The list with fewer total characters. If both lists have the same number of characters, it returns the first list.
- **Examples**:
  - `total_match([], [])` ➞ `[]`
  - `total_match(['hi', 'admin'], ['hI', 'Hi'])` ➞ `['hI', 'Hi']`
  - `total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])` ➞ `['hi', 'admin']`
  - `total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])` ➞ `['hI', 'hi', 'hi']`
  - `total_match(['4'], ['1', '2', '3', '4', '5'])` ➞ `['4']`

## Installation

### Prerequisites

- Python 3.x installed on your system.

### Steps

1. **Clone the Repository**: 
   - Use `git clone <repository-url>` to clone the repository to your local machine.

2. **Navigate to the Project Directory**:
   - Use `cd <project-directory>` to navigate to the directory where the project is located.

3. **Install Dependencies**:
   - The project does not have any external dependencies, so you can skip this step. However, ensure that your Python environment is set up correctly.

## How to Use

1. **Open the `main.py` File**:
   - Locate the `main.py` file in your project directory.

2. **Run the Function**:
   - You can directly call the `total_match` function with your desired lists as arguments.
   - Example:
     ```python
     result = total_match(['hi', 'admin'], ['hI', 'Hi'])
     print(result)  # Output: ['hI', 'Hi']
     ```

3. **Modify and Test**:
   - Feel free to modify the lists in the function calls to test different scenarios.

## Additional Information

- This function is designed to be simple and efficient, focusing solely on comparing the total number of characters in two lists of strings.
- The function does not handle non-string elements in the lists and assumes that all elements are strings.

For any issues or further assistance, please contact the development team.