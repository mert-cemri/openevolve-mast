# Prime Number Finder

This software provides a simple utility to find all prime numbers less than a given non-negative integer `n`. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function of this software is `count_up_to(n)`, which returns a list of prime numbers less than the specified integer `n`.

### Function: `count_up_to(n)`

- **Input**: A non-negative integer `n`.
- **Output**: A list of integers that are prime numbers and less than `n`.

#### Example Usage

```python
print(count_up_to(5))  # Output: [2, 3]
print(count_up_to(11)) # Output: [2, 3, 5, 7]
print(count_up_to(0))  # Output: []
print(count_up_to(20)) # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))  # Output: []
print(count_up_to(18)) # Output: [2, 3, 5, 7, 11, 13, 17]
```

## Installation

This software does not require any external libraries or dependencies, making it straightforward to set up and use.

### Quick Install

1. **Ensure Python is installed**: This software requires Python to run. You can download and install Python from the [official website](https://www.python.org/).

2. **Clone or download the repository**: You can clone the repository using Git or download the ZIP file and extract it.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

   ```bash
   cd path/to/directory
   ```

4. **Run the script**: You can execute the script using Python to see the prime numbers less than a given number.

   ```bash
   python main.py
   ```

## How to Use

1. **Open the `main.py` file**: You can edit the file to include your desired input for the `count_up_to(n)` function.

2. **Run the script**: Use the command line to execute the script and view the output.

3. **Modify and Experiment**: Feel free to modify the code to experiment with different inputs or integrate it into larger projects.

## Documentation

The code is well-commented and should be easy to understand. The `is_prime(num)` function is a helper function used to determine if a number is prime. The `count_up_to(n)` function utilizes this helper function to generate a list of prime numbers.

For further assistance or questions, please refer to the comments within the code or contact the development team.