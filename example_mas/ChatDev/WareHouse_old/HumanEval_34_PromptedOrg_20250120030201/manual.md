# Unique Function User Manual

This manual provides instructions on how to use the `unique` function, which is designed to return sorted unique elements from a list. This function is implemented in Python and does not require any external dependencies.

## Overview

The `unique` function takes a list as input and returns a new list containing only the unique elements from the original list, sorted in ascending order. This is useful for data processing tasks where duplicate values need to be removed and the data needs to be sorted.

## Installation

Since the `unique` function does not require any external libraries, there is no need to install additional dependencies. You only need to have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download it from the official Python website: [python.org](https://www.python.org/). Follow the instructions provided on the website to install Python on your operating system.

## Usage

To use the `unique` function, follow these steps:

1. **Create a Python Script:**

   Create a new Python file, for example, `main.py`, and include the following code:

   ```python
   def unique(l: list):
       """Return sorted unique elements in a list
       >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
       [0, 2, 3, 5, 9, 123]
       """
       return sorted(set(l))
   ```

2. **Call the Function:**

   You can call the `unique` function by passing a list of elements as an argument. For example:

   ```python
   result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
   print(result)  # Output: [0, 2, 3, 5, 9, 123]
   ```

3. **Run the Script:**

   Execute the script using a Python interpreter. Open a terminal or command prompt, navigate to the directory containing your `main.py` file, and run the following command:

   ```bash
   python main.py
   ```

   This will output the sorted list of unique elements.

## Example

Here is a complete example of how to use the `unique` function:

```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage
example_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
unique_elements = unique(example_list)
print("Sorted unique elements:", unique_elements)
```

Running this script will display:

```
Sorted unique elements: [0, 2, 3, 5, 9, 123]
```

This concludes the user manual for the `unique` function. Enjoy using this simple yet powerful tool for processing lists in Python!