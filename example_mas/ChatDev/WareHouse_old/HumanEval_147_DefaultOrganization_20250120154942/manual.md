manual.md

```
# Get Max Triples

## Introduction

The `get_max_triples` function is a Python utility designed to compute the number of valid triples in an integer array derived from a given positive integer `n`. The function generates an array where each element is calculated using the formula `i * i - i + 1` for each index `i` from 1 to `n`. It then counts the number of triples `(a[i], a[j], a[k])` such that `i < j < k` and the sum of the triple is a multiple of 3.

## Main Function

### get_max_triples(n)

- **Input**: A positive integer `n`.
- **Output**: An integer representing the number of valid triples where the sum is a multiple of 3.
- **Example**: 
  - Input: `n = 5`
  - Output: `1`
  - Explanation: The array generated is `[1, 3, 7, 13, 21]`. The only valid triple is `(1, 7, 13)`.

## Installation

This utility does not require any external dependencies, making it straightforward to use in any Python environment.

### Setting Up the Environment

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Clone or Download the Repository**: Obtain the script containing the `get_max_triples` function. You can clone the repository or download the script directly.

3. **No Additional Packages Required**: Since there are no external dependencies, you can directly run the script without any additional installations.

## Usage

To use the `get_max_triples` function, follow these steps:

1. **Open a Terminal or Command Prompt**: Navigate to the directory where the script is located.

2. **Run the Script**: You can execute the script using Python. For example, to test the function with `n = 5`, you can use the following command:

   ```bash
   python -c "from main import get_max_triples; print(get_max_triples(5))"
   ```

   This command will output `1`, which is the number of valid triples for `n = 5`.

3. **Modify and Test**: Feel free to modify the input value `n` to test with different numbers.

## Conclusion

The `get_max_triples` function is a simple yet effective tool for calculating specific triples in an array derived from a mathematical formula. Its ease of use and lack of dependencies make it a versatile utility for various applications.

For further assistance or questions, please contact our support team.
```