# Max Fill User Manual

## Introduction

The `max_fill` function is a Python-based utility designed to calculate the number of times buckets need to be lowered to empty all the wells in a given grid. Each well is represented by a row in the grid, and each '1' in a row represents a single unit of water. The function takes into account the capacity of the buckets used to extract water.

## Main Function

### `max_fill(grid, capacity)`

- **Purpose**: Calculate the number of times buckets need to be lowered to empty all the wells in a grid.
- **Parameters**:
  - `grid`: A list of lists, where each sublist represents a row of wells. Each element in the sublist is either 0 (no water) or 1 (one unit of water).
  - `capacity`: An integer representing the capacity of the bucket, i.e., the number of water units it can hold at once.
- **Returns**: An integer representing the number of times the bucket needs to be lowered to empty all the wells.

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

## Usage

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the `max_fill` function by importing it into your Python script or interactive session. Here is an example of how to use it:

   ```python
   from main import max_fill

   grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
   bucket_capacity = 1
   result = max_fill(grid, bucket_capacity)
   print(f"Number of times to lower the bucket: {result}")
   ```

4. **Test with Different Inputs**: You can test the function with different grid configurations and bucket capacities to see how it performs under various scenarios.

## Examples

- **Example 1**:
  - **Input**: `grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]`, `bucket_capacity = 1`
  - **Output**: `6`
  - **Explanation**: There are 6 units of water in total, and each bucket can hold 1 unit, so the bucket needs to be lowered 6 times.

- **Example 2**:
  - **Input**: `grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]`, `bucket_capacity = 2`
  - **Output**: `5`
  - **Explanation**: There are 10 units of water in total, and each bucket can hold 2 units, so the bucket needs to be lowered 5 times.

- **Example 3**:
  - **Input**: `grid = [[0,0,0], [0,0,0]]`, `bucket_capacity = 5`
  - **Output**: `0`
  - **Explanation**: There are no units of water, so the bucket does not need to be lowered.

## Conclusion

The `max_fill` function is a simple yet effective tool for calculating the number of bucket operations needed to empty a grid of wells. It is easy to integrate into larger applications or use as a standalone utility for specific tasks involving grid-based water extraction simulations.