# Prime Number Finder

This software module provides a simple function to find all prime numbers less than a given non-negative integer `n`. It is designed to be lightweight and does not require any external dependencies.

## Main Functionality

The main function of this software is `count_up_to(n)`, which takes a non-negative integer `n` and returns a list of all prime numbers less than `n`.

### Function Details

- **Function Name:** `count_up_to`
- **Input:** A non-negative integer `n`
- **Output:** A list of prime numbers less than `n`

#### Example Usage

```python
count_up_to(5)    # Returns: [2, 3]
count_up_to(11)   # Returns: [2, 3, 5, 7]
count_up_to(0)    # Returns: []
count_up_to(20)   # Returns: [2, 3, 5, 7, 11, 13, 17, 19]
count_up_to(1)    # Returns: []
count_up_to(18)   # Returns: [2, 3, 5, 7, 11, 13, 17]
```

## Installation

This software does not require any external libraries or dependencies. You only need Python installed on your system to run the function.

### Quick Install

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository:**
   - You can clone the repository using Git or download the ZIP file and extract it to your desired location.

2. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Function:**
   - You can use the function in a Python script or an interactive Python shell. Simply import the function and call it with your desired input.

   ```python
   from main import count_up_to

   # Example usage
   primes = count_up_to(10)
   print(primes)  # Output: [2, 3, 5, 7]
   ```

## Documentation

For further details and examples, refer to the comments within the `main.py` file. The function is straightforward and designed to be easily integrated into other Python projects.

Feel free to modify and adapt the code to suit your specific needs. If you encounter any issues or have suggestions for improvements, please reach out to the development team.