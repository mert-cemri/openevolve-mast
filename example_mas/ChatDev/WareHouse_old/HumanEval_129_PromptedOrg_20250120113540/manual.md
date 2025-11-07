# MinPath User Manual

Welcome to the MinPath software, a Python-based solution for finding the minimum path of a specified length in a grid. This manual will guide you through understanding the main functions of the software, how to install it, and how to use it effectively.

## Overview

MinPath is designed to solve the problem of finding the minimum path of a given length `k` in a grid. The grid is composed of integers ranging from 1 to N*N, where each integer appears exactly once. The software allows you to start from any cell and move to any neighboring cell, ensuring the path is lexicographically minimal.

## Main Function

### `minPath(grid, k)`

- **Purpose**: Finds the minimum path of length `k` in a grid.
- **Parameters**:
  - `grid`: A 2D list representing the grid, where each cell contains a unique integer.
  - `k`: An integer representing the length of the path.
- **Returns**: An ordered list of the values on the cells that the minimum path goes through.

## Installation

MinPath does not require any external dependencies, making it easy to set up and use. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download the source code from the repository or copy the `main.py` file to your local directory.

2. **Set Up Environment**: Since there are no external dependencies, you can directly run the script using Python.

## Usage

To use the MinPath function, follow these steps:

1. **Prepare Your Grid**: Define a grid as a 2D list where each integer from 1 to N*N appears exactly once.

2. **Call the Function**: Use the `minPath` function by passing your grid and the desired path length `k`.

3. **Example**:

   ```python
   grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   k = 3
   result = minPath(grid, k)
   print(result)  # Output: [1, 2, 1]
   ```

## Documentation

For further details on the implementation and examples, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the function.

## Support

If you encounter any issues or have questions about using MinPath, please feel free to reach out to our support team. We are here to assist you in making the most out of this software.

Thank you for choosing MinPath! We hope it meets your needs and helps you solve your grid path problems efficiently.