# Move One Ball User Manual

Welcome to the Move One Ball software! This tool is designed to help you determine if an array of integers can be sorted in non-decreasing order by performing right shift operations. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it.

## Quick Install

To use the Move One Ball software, you need to have Python installed on your system. If you haven't installed Python yet, please download and install it from [python.org](https://www.python.org/).

### Installation Steps

1. **Clone the Repository**: First, clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Although there are no additional dependencies required for this project, ensure your Python environment is set up correctly.

## Main Functionality

The core functionality of the Move One Ball software is encapsulated in the `move_one_ball` function. This function checks if an array can be sorted in non-decreasing order by performing right shift operations.

### Function Definition

```python
def move_one_ball(arr):
    if not arr:
        return True
    n = len(arr)
    break_point = -1
    # Find the point where the array is not sorted
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            if break_point != -1:
                return False
            break_point = i
    # If the array is already sorted
    if break_point == -1:
        return True
    # Check if the array can be sorted by shifting from the break point
    for i in range(break_point, n):
        if i < n - 1 and arr[i] > arr[i + 1]:
            return False
    # Check if the last element is less than or equal to the first element of the sorted part
    if arr[n - 1] > arr[0]:
        return False
    return True
```

### How It Works

- **Input**: An array of unique integers.
- **Output**: Returns `True` if the array can be sorted in non-decreasing order using right shift operations, otherwise returns `False`.
- **Edge Cases**: If the array is empty, the function returns `True`.

## How to Use

1. **Open the Terminal**: Navigate to the directory where the `main.py` file is located.

2. **Run the Python Script**: Execute the script using Python. You can test the function with different arrays by modifying the input in the script.
   ```bash
   python main.py
   ```

3. **Example Usage**:
   - To check if the array `[3, 4, 5, 1, 2]` can be sorted:
     ```python
     print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
     ```
   - To check if the array `[3, 5, 4, 1, 2]` can be sorted:
     ```python
     print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False
     ```

## Conclusion

The Move One Ball software provides a simple yet effective way to determine the possibility of sorting an array using right shift operations. We hope this manual helps you understand and utilize the software effectively. If you have any questions or need further assistance, please feel free to reach out.