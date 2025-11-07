# Prime Number Finder

This software module provides a simple utility to find prime numbers less than a given non-negative integer. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main functionality of this software is encapsulated in the `count_up_to` function. This function takes a non-negative integer `n` as input and returns a list of all prime numbers less than `n`.

### Function: `count_up_to(n)`

- **Input:** A non-negative integer `n`.
- **Output:** A list of prime numbers less than `n`.

#### Example Usage

```python
# Example usage:
print(count_up_to(5))  # Output: [2, 3]
print(count_up_to(11)) # Output: [2, 3, 5, 7]
print(count_up_to(0))  # Output: []
print(count_up_to(20)) # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))  # Output: []
print(count_up_to(18)) # Output: [2, 3, 5, 7, 11, 13, 17]
```

## Installation

This software does not require any external libraries or dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Requirements

- Python 3.x

### Installation Steps

1. **Clone the Repository:**
   - Clone the repository to your local machine using the following command:
     ```bash
     git clone <repository-url>
     ```

2. **Navigate to the Directory:**
   - Change into the directory where the `main.py` file is located:
     ```bash
     cd <repository-directory>
     ```

3. **Run the Script:**
   - You can run the script directly using Python:
     ```bash
     python main.py
     ```

## How to Use

1. **Import the Function:**
   - You can import the `count_up_to` function into your own Python scripts or use it directly in the Python interactive shell.

2. **Call the Function:**
   - Pass a non-negative integer to the `count_up_to` function to get a list of prime numbers less than the given integer.

## Documentation

For further details on the implementation and usage, please refer to the comments within the `main.py` file. The code is straightforward and includes inline comments to help you understand its functionality.

This software is designed to be simple and efficient, providing a quick way to find prime numbers for educational purposes or small-scale applications.