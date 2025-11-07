# Triple Sum Checker

This software is designed to calculate the number of valid triples from an array where the sum of the triple is a multiple of 3. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function of this software is `get_max_triples(n)`, which performs the following tasks:

1. **Generate an Array**: Creates an integer array `a` of length `n` where each element `a[i]` is calculated using the formula `i * i - i + 1` for each `i` in the range from 1 to `n`.

2. **Count Valid Triples**: Counts the number of triples `(a[i], a[j], a[k])` such that `i < j < k` and the sum `a[i] + a[j] + a[k]` is a multiple of 3.

3. **Return the Count**: Returns the count of such valid triples.

## Installation

This software does not require any external libraries or dependencies. It is implemented using pure Python, and you can run it in any Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Script**: Execute the script using Python. You can do this by running the following command in your terminal:

   ```bash
   python main.py
   ```

4. **Call the Function**: You can call the `get_max_triples(n)` function with your desired value of `n` to get the number of valid triples. For example:

   ```python
   result = get_max_triples(5)
   print(result)  # Output: 1
   ```

## Example

Here is an example of how to use the function:

```python
def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

# Example usage
n = 5
print(get_max_triples(n))  # Output: 1
```

This example demonstrates how to calculate the number of valid triples for `n = 5`, which results in an output of `1`.

## Conclusion

This software provides a simple and efficient way to calculate the number of valid triples in an array where the sum is a multiple of 3. It is easy to use and does not require any additional setup beyond having Python installed.