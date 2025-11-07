manual.md

```
# Rescale to Unit

This software provides a simple function to rescale a list of numbers such that the smallest number becomes 0 and the largest becomes 1. This is useful for normalizing data in various applications, such as data analysis, machine learning, and more.

## Main Function

The main function provided by this software is `rescale_to_unit`. It takes a list of floating-point numbers as input and returns a new list where the numbers are linearly transformed to fit within the range [0, 1].

### Function Signature

```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
```

### Example Usage

```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```

## Installation

To use this software, you need to have Python installed on your system. The function does not require any additional dependencies, so you can directly use it in your Python environment.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the script**: You can directly run the `main.py` file in your Python environment.

## How to Use

1. **Import the Function**: If you are integrating this function into another project, you can import it as follows:
   ```python
   from main import rescale_to_unit
   ```

2. **Call the Function**: Pass a list of numbers to the function to get the rescaled list.
   ```python
   numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   rescaled_numbers = rescale_to_unit(numbers)
   print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
   ```

## Additional Information

- **No External Dependencies**: This function does not rely on any external libraries beyond Python's standard library.
- **Error Handling**: Ensure that the list contains at least two elements to avoid division by zero errors.

For further assistance or inquiries, please contact our support team.
```