# Sort Array Application

This application provides a function to sort an array of non-negative integers based on specific criteria. The sorting order is determined by the sum of the first and last elements of the array.

## Main Functionality

The main function of this software is `sort_array(array)`, which performs the following operations:

- **Input:** An array of non-negative integers.
- **Output:** A sorted copy of the input array.
  - If the sum of the first and last elements is odd, the array is sorted in ascending order.
  - If the sum is even, the array is sorted in descending order.
- **Note:** The original array is not modified.

### Examples

- `sort_array([])` returns `[]`
- `sort_array([5])` returns `[5]`
- `sort_array([2, 4, 3, 0, 1, 5])` returns `[0, 1, 2, 3, 4, 5]`
- `sort_array([2, 4, 3, 0, 1, 5, 6])` returns `[6, 5, 4, 3, 2, 1, 0]`

## Installation

This application does not require any external dependencies. It is implemented purely in Python. To use the function, ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**
   - Clone the repository to your local machine using `git clone <repository-url>`.
   
2. **Navigate to the Directory:**
   - Change into the directory where the `main.py` file is located.

3. **Run the Code:**
   - You can run the code directly using Python. Open a terminal and execute:
     ```bash
     python main.py
     ```

## How to Use

1. **Import the Function:**
   - To use the `sort_array` function in your own Python script, import it as follows:
     ```python
     from main import sort_array
     ```

2. **Call the Function:**
   - Pass an array of non-negative integers to the function:
     ```python
     result = sort_array([2, 4, 3, 0, 1, 5])
     print(result)  # Output: [0, 1, 2, 3, 4, 5]
     ```

## Documentation

For further details and examples, refer to the inline documentation within the `main.py` file. The function is self-contained and does not require additional setup beyond having Python installed.

Feel free to modify and extend the function as needed for your specific use cases.