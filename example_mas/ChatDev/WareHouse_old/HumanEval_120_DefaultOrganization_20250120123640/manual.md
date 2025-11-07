# Maximum K Elements Finder

This software provides a simple function to find the maximum `k` numbers from a given array of integers. The function is designed to return these numbers in sorted order.

## Main Functionality

The main function provided by this software is `maximum(arr, k)`. This function takes two inputs:
- `arr`: A list of integers.
- `k`: A positive integer representing the number of maximum elements to return.

The function returns a sorted list of the `k` largest numbers from the input array `arr`.

### Example Usage

1. **Example 1:**
   - **Input:** `arr = [-3, -4, 5]`, `k = 3`
   - **Output:** `[-4, -3, 5]`

2. **Example 2:**
   - **Input:** `arr = [4, -4, 4]`, `k = 2`
   - **Output:** `[4, 4]`

3. **Example 3:**
   - **Input:** `arr = [-3, 2, 1, 2, -1, -2, 1]`, `k = 1`
   - **Output:** `[2]`

## Installation

This software does not require any external dependencies, making it straightforward to use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**
   - You can clone the repository to your local machine using:
     ```bash
     git clone <repository-url>
     ```

2. **Navigate to the Directory:**
   - Change your directory to where the `main.py` file is located:
     ```bash
     cd <repository-directory>
     ```

3. **Run the Function:**
   - You can directly run the function in a Python environment or script by importing it:
     ```python
     from main import maximum

     # Example usage
     result = maximum([-3, -4, 5], 3)
     print(result)  # Output: [-4, -3, 5]
     ```

## How to Use

1. **Import the Function:**
   - Ensure you import the `maximum` function from the `main.py` file.

2. **Call the Function:**
   - Pass the array and the integer `k` as arguments to the function.

3. **Receive the Output:**
   - The function will return a sorted list of the maximum `k` numbers from the array.

## Additional Notes

- The length of the array `arr` should be between 1 and 1000.
- The elements in the array should be between -1000 and 1000.
- The value of `k` should be between 0 and the length of the array.

This software is designed to be simple and efficient, providing a quick solution for finding the maximum `k` numbers in an array. Enjoy using it!