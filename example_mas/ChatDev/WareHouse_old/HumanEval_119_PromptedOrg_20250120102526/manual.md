# Match Parens User Manual

## Introduction

The `match_parens` function is a simple utility designed to determine if two strings of parentheses can be concatenated in some order to form a balanced string. A string is considered balanced if every opening parenthesis '(' has a corresponding closing parenthesis ')'.

### Main Function

- **match_parens(lst):** This function takes a list of two strings, each consisting of only open '(' and close ')' parentheses. It checks if there is a way to concatenate these two strings such that the resulting string is balanced. It returns 'Yes' if possible, and 'No' otherwise.

## Installation

### Environment Setup

This project does not require any external dependencies, making it straightforward to set up and run. You only need Python installed on your system.

### Python Installation

Ensure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

### Running the Code

1. **Clone the Repository:**
   - If the code is hosted in a repository, clone it using:
     ```bash
     git clone <repository-url>
     ```
   - Navigate to the project directory:
     ```bash
     cd <project-directory>
     ```

2. **Run the Script:**
   - You can run the `main.py` file directly using Python:
     ```bash
     python main.py
     ```

## Usage

To use the `match_parens` function, you can call it with a list of two strings as an argument. Here are some examples:

```python
# Example 1
result = match_parens(['()(', ')'])
print(result)  # Output: 'Yes'

# Example 2
result = match_parens([')', ')'])
print(result)  # Output: 'No'
```

### Explanation

- **Example 1:** The strings `'()('` and `')'` can be concatenated to form `'()()'`, which is balanced. Hence, the function returns 'Yes'.
- **Example 2:** The strings `')'` and `')'` cannot be concatenated in any order to form a balanced string. Hence, the function returns 'No'.

## Conclusion

The `match_parens` function is a simple yet effective tool for checking the balance of parentheses in concatenated strings. With no external dependencies, it is easy to integrate into any Python project where such functionality is needed.