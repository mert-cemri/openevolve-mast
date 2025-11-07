# Max Fill User Manual

Welcome to the Max Fill software, a simple yet effective tool designed to calculate the number of times buckets need to be lowered to empty the wells in a given grid. This manual will guide you through the main functions of the software, how to install it, and how to use it effectively.

## Main Functions

The primary function of this software is `max_fill`, which calculates the number of times buckets need to be lowered to empty the wells in a grid. The grid is represented as a list of lists, where each `1` represents a unit of water. The function takes two parameters:

- `grid`: A list of lists of integers, where each `1` represents a unit of water.
- `capacity`: An integer representing the capacity of the bucket.

The function returns an integer, which is the number of times the bucket needs to be lowered to empty all the wells in the grid.

## Installation

### Environment Setup

This software does not require any external dependencies. However, you need to have Python installed on your system. You can download and install Python from the official website: [python.org](https://www.python.org/).

### Quick Install

Since there are no external dependencies, you can directly use the software by downloading the `main.py` file and running it in your Python environment.

## How to Use

1. **Prepare the Grid and Capacity:**
   - Define your grid as a list of lists, where each sublist represents a row in the grid, and each element is either `0` or `1`.
   - Define the capacity of the bucket as an integer.

2. **Run the Function:**
   - Import the `max_fill` function from the `main.py` file.
   - Call the `max_fill` function with your grid and capacity as arguments.

3. **Example Usage:**

   ```python
   from main import max_fill

   grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
   capacity = 1

   result = max_fill(grid, capacity)
   print(result)  # Output: 6
   ```

4. **Interpret the Result:**
   - The output will be an integer representing the number of times the bucket needs to be lowered to empty all the wells in the grid.

## Conclusion

The Max Fill software provides a straightforward solution to calculate the number of bucket lowerings required to empty a grid of wells. With no external dependencies, it is easy to set up and use. Simply define your grid and bucket capacity, and let the software do the rest. Enjoy using Max Fill to solve your water extraction problems efficiently!