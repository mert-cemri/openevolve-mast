# MinSubArraySum

A Python function to find the minimum sum of any non-empty sub-array of a given list of integers.

## Quick Install

This project does not require any external dependencies. You only need Python installed on your system to run the code.

## 🤔 What is this?

The `minSubArraySum` function is designed to solve the problem of finding the minimum sum of any non-empty sub-array from a list of integers. This can be useful in various computational problems where you need to determine the smallest possible sum of contiguous elements in an array.

## 📖 How to Use

### Function Description

The `minSubArraySum` function takes a list of integers as input and returns the minimum sum of any non-empty sub-array.

#### Example

```python
minSubArraySum([2, 3, 4, 1, 2, 4])  # Returns 1
minSubArraySum([-1, -2, -3])        # Returns -6
```

### How to Run

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Python File**: Save the provided code in a file named `main.py`.

3. **Run the Code**: Open a terminal or command prompt, navigate to the directory where `main.py` is located, and run the following command:

   ```bash
   python main.py
   ```

4. **Test the Function**: You can test the function by calling it with different lists of integers and observing the output.

### Code Explanation

The function uses a simple algorithm to iterate through the list of integers, maintaining a running sum of the current sub-array. It keeps track of the minimum sum encountered and resets the current sum to zero if it becomes positive, ensuring that only the smallest possible sub-array sums are considered.

## 🚀 Getting Started

To get started with using the `minSubArraySum` function, simply copy the code into your Python environment and call the function with your desired list of integers. The function will return the minimum sum of any non-empty sub-array.

```python
def minSubArraySum(nums):
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > 0:
            current_sum = 0
    return min_sum
```

This function is efficient and works well for lists of various sizes, providing a quick and reliable way to find the minimum sub-array sum.