manual.md

```
# Get Max Triples

This software provides a function to calculate the number of triples in an array where the sum of the elements in each triple is a multiple of 3. The array is generated based on a given positive integer `n`.

## Main Functionality

The main functionality of this software is encapsulated in the function `get_max_triples(n)`. This function performs the following tasks:

1. **Array Generation**: Creates an integer array `a` of length `n` where each element `a[i]` is calculated using the formula `a[i] = i * i - i + 1`.

2. **Triple Calculation**: Iterates through all possible triples `(a[i], a[j], a[k])` in the array where `i < j < k` and counts the number of triples where the sum `a[i] + a[j] + a[k]` is a multiple of 3.

3. **Return Value**: Returns the count of such valid triples.

## Installation

This software does not require any external dependencies, so there is no need for a `requirements.txt` file. You can run the script directly using Python.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Script**: Execute the script using Python. You can do this by running the following command in your terminal:

   ```bash
   python main.py
   ```

   This will execute the example usage of the `get_max_triples` function with `n = 5`, and it should output `1`.

4. **Modify Input**: To test with different values of `n`, you can modify the `print(get_max_triples(n))` line in the `main.py` file with your desired input value.

## Example

Here's an example of how the function works:

- **Input**: `n = 5`
- **Generated Array**: `a = [1, 3, 7, 13, 21]`
- **Valid Triple**: The only valid triple is `(1, 7, 13)` because `1 + 7 + 13 = 21`, which is a multiple of 3.
- **Output**: `1`

This software provides a simple yet effective way to calculate the number of valid triples in an array based on the given conditions.

```