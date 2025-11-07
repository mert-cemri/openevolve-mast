manual.md

```
# Max Fill Software

This software provides a function to calculate the number of times buckets need to be lowered to empty the wells represented by a grid. Each well is represented by a row in the grid, and each '1' in a row represents a single unit of water. The software is designed to efficiently determine how many times buckets of a given capacity need to be used to remove all the water from the wells.

## Main Functionality

The main function provided by this software is `max_fill(grid, capacity)`, which calculates the number of times buckets need to be lowered to empty the wells.

### Function Details

- **Function Name:** `max_fill`
- **Parameters:**
  - `grid` (list of list of int): A rectangular grid where each '1' represents a unit of water.
  - `capacity` (int): The capacity of each bucket.
- **Returns:** 
  - `int`: The number of times buckets need to be lowered.

### Example Usage

```python
# Example 1
print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))  # Output: 6

# Example 2
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))  # Output: 5

# Example 3
print(max_fill([[0,0,0], [0,0,0]], 5))  # Output: 0
```

## Installation

This software does not require any external dependencies, making it simple to set up and use. You can directly use the provided Python script without any additional installation steps.

### Requirements

- Python 3.x

### Installation Steps

1. **Clone the Repository:**
   - Clone the repository to your local machine using the following command:
     ```bash
     git clone <repository-url>
     ```

2. **Navigate to the Directory:**
   - Change into the directory containing the `main.py` file:
     ```bash
     cd <repository-directory>
     ```

3. **Run the Script:**
   - You can run the script directly using Python:
     ```bash
     python main.py
     ```

## How to Use

1. **Prepare Your Grid and Capacity:**
   - Define your grid as a list of lists, where each sublist represents a row of wells, and each '1' represents a unit of water.
   - Define the capacity of the bucket as an integer.

2. **Call the `max_fill` Function:**
   - Pass your grid and bucket capacity to the `max_fill` function to get the number of times buckets need to be lowered.

3. **Interpret the Output:**
   - The function will return an integer representing the number of times the buckets need to be lowered to empty all the wells.

This software provides a simple and efficient way to calculate the number of bucket operations needed for a given grid of wells and bucket capacity. Enjoy using the Max Fill Software!
```