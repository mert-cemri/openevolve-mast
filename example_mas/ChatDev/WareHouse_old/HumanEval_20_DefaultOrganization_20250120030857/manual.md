# Find Closest Elements

This software module provides a function to find the two closest numbers in a list of floating-point numbers. It is designed to be simple and efficient, requiring no external dependencies.

## Main Function

The primary function of this software is `find_closest_elements`, which takes a list of floating-point numbers and returns a tuple containing the two numbers that are closest to each other in the list. The numbers in the tuple are returned in ascending order.

### Function Signature

```python
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
```

### Example Usage

```python
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
(2.0, 2.2)

>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
(2.0, 2.0)
```

## Installation

This software does not require any external dependencies, making it straightforward to use. Simply ensure you have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download it from [python.org](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## How to Use

1. **Clone or Download the Repository:**
   - You can clone the repository using Git or download the files directly.

2. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Function:**
   - You can use the function in a Python script or an interactive Python session. Simply import the function and pass a list of numbers to it.

### Example Script

```python
from main import find_closest_elements

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
closest_pair = find_closest_elements(numbers)
print(f"The closest pair of numbers is: {closest_pair}")
```

## Documentation

For further details and documentation, you can refer to the docstring within the `main.py` file, which provides a concise explanation of the function's purpose and usage.

## Support

If you encounter any issues or have questions about using this software, please feel free to reach out for support. We are committed to ensuring a smooth and effective experience with our software.