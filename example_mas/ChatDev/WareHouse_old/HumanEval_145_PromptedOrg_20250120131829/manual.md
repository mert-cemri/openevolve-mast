# Order By Points

This software provides a function `order_by_points` that sorts a list of integers based on the sum of their digits. If two numbers have the same digit sum, they are ordered based on their original position in the list.

## Main Functionality

### `order_by_points`

- **Description**: This function sorts a given list of integers in ascending order according to the sum of their digits. If there are several items with similar sum of their digits, they are ordered based on their index in the original list.
- **Arguments**: 
  - `nums` (list of int): The list of integers to sort.
- **Returns**: 
  - `list of int`: The sorted list of integers.

### Example Usage

```python
# Example usage of the order_by_points function
print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
print(order_by_points([]))  # Output: []
```

## Installation

### Environment Setup

This software does not require any external dependencies, making it easy to set up and use. You can run the code in any Python environment.

### Requirements

- Python 3.x

### Installation Steps

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

3. **Run the Code**: You can directly run the `main.py` file in your Python environment.
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you are using this function in another script, make sure to import it.
   ```python
   from main import order_by_points
   ```

2. **Call the Function**: Pass a list of integers to the `order_by_points` function to get the sorted list.
   ```python
   sorted_list = order_by_points([1, 11, -1, -11, -12])
   print(sorted_list)  # Output: [-1, -11, 1, -12, 11]
   ```

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The code is self-explanatory and includes detailed comments to guide you through its functionality.

This manual provides all the necessary information to understand and use the `order_by_points` function effectively. If you have any questions or need further assistance, please feel free to reach out.