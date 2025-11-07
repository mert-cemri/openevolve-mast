# MinSubArraySum

A Python function to find the minimum sum of any non-empty sub-array of integers.

## Introduction

The `minSubArraySum` function is designed to solve the problem of finding the minimum sum of any non-empty sub-array within a given list of integers. This can be useful in various computational problems where identifying the smallest possible sum of contiguous elements is required.

### Main Functionality

- **Function Name:** `minSubArraySum`
- **Input:** A list of integers `nums`.
- **Output:** An integer representing the minimum sum of any non-empty sub-array of `nums`.

### Example Usage

```python
minSubArraySum([2, 3, 4, 1, 2, 4])  # Output: 1
minSubArraySum([-1, -2, -3])        # Output: -6
```

## Installation

This function does not require any external dependencies, making it straightforward to use. You only need Python installed on your system.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository:**

   You can clone the repository using Git or download the ZIP file and extract it.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Open a terminal and navigate to the directory where the `main.py` file is located.

   ```bash
   cd path/to/directory
   ```

3. **Run the Function:**

   You can run the function by executing the `main.py` file in a Python environment.

   ```bash
   python main.py
   ```

4. **Modify the Input:**

   You can modify the input list in the `main.py` file to test with different arrays of integers.

## Documentation

The function is implemented in a straightforward manner using a variation of Kadane's algorithm, which efficiently finds the minimum sum of a sub-array in linear time.

### Function Explanation

- **Initialization:**
  - `min_ending_here` and `min_so_far` are initialized to the first element of the array.
  
- **Iteration:**
  - For each element in the array, update `min_ending_here` to be the minimum of the current element or the sum of `min_ending_here` and the current element.
  - Update `min_so_far` to be the minimum of itself and `min_ending_here`.

- **Return Value:**
  - The function returns `min_so_far`, which holds the minimum sum of any sub-array found.

This approach ensures that the function runs efficiently even for large arrays, making it suitable for a wide range of applications.