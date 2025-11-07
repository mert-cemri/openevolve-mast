# Find Closest Elements

This software module provides a function to find the two closest numbers in a list of floating-point numbers. It is designed to be simple and efficient, ensuring that users can easily integrate it into their Python projects.

## Main Functionality

The main function provided by this module is `find_closest_elements`. This function takes a list of floating-point numbers and returns a tuple containing the two numbers that are closest to each other. The numbers in the tuple are returned in ascending order.

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

To use this module, you need to have Python installed on your system. The module does not have any external dependencies, so you do not need to install any additional packages.

### Quick Install

Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your working directory to where the `main.py` file is located.

   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: You can run the code using Python to test its functionality.

   ```bash
   python main.py
   ```

4. **Integrate into Your Project**: You can import the `find_closest_elements` function into your own Python projects.

   ```python
   from main import find_closest_elements

   closest_pair = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
   print(closest_pair)  # Output: (2.0, 2.2)
   ```

## Documentation

For further documentation and examples, please refer to the inline comments and docstrings within the `main.py` file. These provide detailed explanations of the function's logic and usage.

## Support

If you encounter any issues or have questions about using this module, please feel free to reach out to our support team or open an issue in the repository if applicable.