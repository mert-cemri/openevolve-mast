# Make a Pile

This software provides a simple function to create a pile of stones with a specified number of levels. Each level has a specific number of stones, following a pattern based on whether the initial number of stones is odd or even.

## Main Function

### `make_a_pile(n)`

- **Description**: Given a positive integer `n`, this function creates a pile of `n` levels of stones. The first level has `n` stones. The number of stones in the next level is:
  - The next odd number if the current number of stones is odd.
  - The next even number if the current number of stones is even.
- **Parameters**: 
  - `n` (int): A positive integer representing the number of levels in the pile.
- **Returns**: 
  - A list where each element at index `i` represents the number of stones in the level `(i+1)`.

#### Example
```python
>>> make_a_pile(3)
[3, 5, 7]
```

## Installation

This project does not require any external dependencies. You can use the function directly in your Python environment.

### Quick Start

1. **Clone the Repository**: 
   - Clone the repository to your local machine using Git or download the source code directly.

2. **Navigate to the Project Directory**:
   - Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**:
   - You can use the function in a Python script or an interactive Python session.

## Usage

To use the `make_a_pile` function, simply import it into your Python script or interactive session and call it with the desired number of levels.

### Example Usage

```python
from main import make_a_pile

# Create a pile with 5 levels
pile = make_a_pile(5)
print(pile)  # Output: [5, 7, 9, 11, 13]
```

## Documentation

For further details on how the function works, refer to the docstring provided within the `main.py` file. The function is straightforward and does not require additional configuration or setup.

Feel free to modify the code to suit your specific needs or integrate it into larger projects. If you have any questions or need support, please reach out to our development team.