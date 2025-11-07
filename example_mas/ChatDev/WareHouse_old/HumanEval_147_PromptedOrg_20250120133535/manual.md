# Get Max Triples

This software provides a function to calculate the number of valid triples from an integer array, where each element is defined by a specific formula. The goal is to find triples whose sum is a multiple of 3.

## Main Functionality

The main function of this software is `get_max_triples(n)`. It performs the following tasks:

- Generates an integer array `a` of length `n`, where each element `a[i]` is calculated using the formula: `a[i] = i * i - i + 1`.
- Counts the number of triples `(a[i], a[j], a[k])` such that `i < j < k` and the sum `a[i] + a[j] + a[k]` is a multiple of 3.
- Returns the count of such valid triples.

### Example

For an input `n = 5`, the function generates the array `a = [1, 3, 7, 13, 21]`. The only valid triple is `(1, 7, 13)`, so the function returns `1`.

## Installation

This software does not require any external dependencies. You can directly use the function in your Python environment.

## Usage

To use the `get_max_triples` function, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the function code into your Python script or interactive environment.
3. Call the function with a positive integer `n` as an argument.

### Example Usage

```python
def get_max_triples(n):
    # Generate the array a
    a = [i * i - i + 1 for i in range(1, n + 1)]
    # Count valid triples
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

# Example call
result = get_max_triples(5)
print(result)  # Output: 1
```

## Documentation

The function is straightforward and does not require additional libraries or complex setup. Simply ensure your Python environment is ready, and you can start using the function as demonstrated in the example above.