# Histogram Function User Manual

## Introduction

The Histogram function is a simple Python utility designed to analyze a string of space-separated lowercase letters and return a dictionary indicating the letter(s) with the highest frequency of occurrence. This function is useful for text analysis tasks where understanding the frequency of specific characters is necessary.

## Main Functionality

- **Function Name:** `histogram`
- **Input:** A string of space-separated lowercase letters.
- **Output:** A dictionary where the keys are the letters with the highest frequency and the values are their respective counts.

### Example Usage

- `histogram('a b c')` returns `{'a': 1, 'b': 1, 'c': 1}`
- `histogram('a b b a')` returns `{'a': 2, 'b': 2}`
- `histogram('a b c a b')` returns `{'a': 2, 'b': 2}`
- `histogram('b b b b a')` returns `{'b': 4}`
- `histogram('')` returns `{}`

## Installation

This function does not require any external dependencies, making it easy to integrate into any Python environment.

### Quick Install

Since there are no external dependencies, you can directly use the function in any Python environment. Simply ensure you have Python installed on your system.

1. **Python Installation:** If you do not have Python installed, download and install it from [python.org](https://www.python.org/).

2. **Using the Function:**
   - Copy the code provided in the `main.py` file into your Python script or interactive environment.

## How to Use

1. **Copy the Function:**
   - Copy the `histogram` function from the `main.py` file into your Python script.

2. **Call the Function:**
   - Use the `histogram` function by passing a string of space-separated lowercase letters as an argument.

3. **Analyze the Output:**
   - The function will return a dictionary with the letter(s) that have the highest frequency and their respective counts.

### Example Code

```python
def histogram(test):
    # Split the input string into a list of letters
    letters = test.split()
    # Create a dictionary to count occurrences of each letter
    frequency = {}
    for letter in letters:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    # Find the maximum frequency
    max_count = max(frequency.values(), default=0)
    # Create a result dictionary with letters having the maximum frequency
    result = {letter: count for letter, count in frequency.items() if count == max_count}
    return result

# Example usage
print(histogram('a b c a b'))  # Output: {'a': 2, 'b': 2}
```

## Conclusion

The Histogram function is a straightforward tool for counting the frequency of letters in a string. With no external dependencies, it is easy to integrate and use in any Python project. This function is ideal for quick text analysis tasks where understanding character frequency is essential.