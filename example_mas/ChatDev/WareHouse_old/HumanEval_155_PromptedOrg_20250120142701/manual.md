# Even Odd Count Function

This software provides a simple utility function to count the number of even and odd digits in an integer. It is designed to be straightforward and easy to use, making it ideal for quick calculations or integration into larger projects.

## Main Functionality

The main function provided by this software is `even_odd_count(num)`. This function takes an integer as input and returns a tuple containing two elements:
- The first element is the count of even digits in the integer.
- The second element is the count of odd digits in the integer.

### Example Usage

```python
result = even_odd_count(-12)
print(result)  # Output: (1, 1)

result = even_odd_count(123)
print(result)  # Output: (1, 2)
```

## Installation

This software is implemented in Python and does not require any external dependencies beyond the standard Python library. To use this function, simply ensure you have Python installed on your system.

### Installing Python

If you do not have Python installed, you can download it from the official Python website: [python.org](https://www.python.org/). Follow the instructions for your operating system to install Python.

## How to Use

1. **Download the Code**: Copy the code provided in the `main.py` file and save it to your local machine.

2. **Run the Code**: You can run the code using any Python interpreter. Open a terminal or command prompt, navigate to the directory where your `main.py` file is located, and execute the following command:

   ```bash
   python main.py
   ```

3. **Integrate into Your Project**: If you wish to use the `even_odd_count` function in your own project, simply import the function from the `main.py` file:

   ```python
   from main import even_odd_count

   # Now you can use the function in your project
   result = even_odd_count(4567)
   print(result)  # Output: (2, 2)
   ```

## Conclusion

This software provides a simple yet effective way to count even and odd digits in an integer. It is easy to integrate into existing projects or use as a standalone utility. With no external dependencies, it is lightweight and efficient, making it a great tool for developers working with numerical data.