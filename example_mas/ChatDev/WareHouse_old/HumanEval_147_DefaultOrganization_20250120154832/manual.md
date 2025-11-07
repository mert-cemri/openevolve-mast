# Max Triples Software

This software provides a function to calculate the number of triples from an array where the sum of the elements in each triple is a multiple of 3. The array is generated based on a given positive integer `n`.

## Main Function

### `get_max_triples(n)`

- **Description**: 
  - This function generates an integer array `a` of length `n`.
  - For each index `i` (1 ≤ i ≤ n), the value of `a[i]` is calculated as `i * i - i + 1`.
  - It returns the number of triples `(a[i], a[j], a[k])` where `i < j < k` and the sum `a[i] + a[j] + a[k]` is a multiple of 3.

- **Parameters**:
  - `n` (int): A positive integer representing the length of the array.

- **Returns**:
  - `count` (int): The number of valid triples.

- **Example**:
  ```python
  get_max_triples(5)
  # Output: 1
  # Explanation: a = [1, 3, 7, 13, 21]
  # The only valid triple is (1, 7, 13).
  ```

## Installation

This software does not require any external dependencies. It is implemented purely in Python. Ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**:
   - Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**:
   - Clone the repository to your local machine using:
     ```bash
     git clone <repository-url>
     ```

3. **Navigate to the Directory**:
   - Change into the directory where the code is located:
     ```bash
     cd <repository-directory>
     ```

## Usage

1. **Run the Function**:
   - You can run the function by executing the `main.py` file in a Python environment.
   - Example:
     ```bash
     python main.py
     ```

2. **Modify the Input**:
   - You can modify the input `n` directly in the `main.py` file to test different scenarios.

## Documentation

For further details on how the function works, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic behind the implementation.

This software is designed to be simple and efficient, focusing solely on solving the problem as described without any additional features or interfaces.