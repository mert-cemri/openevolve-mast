# MinPath User Manual

Welcome to the MinPath software! This tool is designed to find the minimum lexicographical path of a specified length in a given grid. This document will guide you through the main functions of the software, how to install the necessary environment dependencies, and how to use the software effectively.

## Main Functions

The primary function of this software is `minPath`, which calculates the minimum path of a specified length `k` in a grid. The grid is a 2D list where each cell contains a unique integer value. The path is determined based on lexicographical order, ensuring that the path is the smallest possible in terms of the values it traverses.

### Functionality

- **Input**: 
  - `grid`: A 2D list of integers where each integer in the range [1, N * N] appears exactly once.
  - `k`: A positive integer representing the length of the path.

- **Output**: 
  - A list of integers representing the values on the cells that the minimum path goes through.

- **Examples**:
  - Input: `grid = [[1,2,3], [4,5,6], [7,8,9]], k = 3`
    - Output: `[1, 2, 1]`
  - Input: `grid = [[5,9,3], [4,1,6], [7,8,2]], k = 1`
    - Output: `[1]`

## Installation

### Environment Setup

The software does not require any external dependencies, making it straightforward to set up. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the Repository**: If the software is hosted on a version control system like GitHub, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**:

   ```bash
   cd <project-directory>
   ```

4. **Run the Software**: You can execute the `main.py` file directly to use the `minPath` function.

   ```bash
   python main.py
   ```

## Usage

To use the `minPath` function, you need to call it with the appropriate grid and path length `k`. Here is an example of how to use the function in a Python script:

```python
from main import minPath

# Define the grid and path length
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 3

# Call the function
result = minPath(grid, k)

# Output the result
print("Minimum Path:", result)
```

## Documentation

For further details on the implementation and examples, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the function.

## Support

If you encounter any issues or have questions, please reach out to our support team or consult the community forums for assistance.

Thank you for using MinPath! We hope this tool meets your needs and enhances your productivity.