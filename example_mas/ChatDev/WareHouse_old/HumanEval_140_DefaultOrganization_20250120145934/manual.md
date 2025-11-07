manual.md

```
# Fix Spaces Utility

A simple Python utility to process strings by replacing spaces with underscores and consecutive spaces with a hyphen.

## Overview

The `fix_spaces` function is designed to modify a given string by:
- Replacing all spaces with underscores.
- Replacing more than two consecutive spaces with a hyphen.

This utility is useful for formatting strings where spaces need to be standardized or removed for consistency, such as in filenames or identifiers.

## Installation

### Prerequisites

- Python 3.x

### Quick Install

No external dependencies are required for this utility. Ensure you have Python installed on your system.

## Usage

### Function: `fix_spaces`

#### Description

The `fix_spaces` function takes a single string input and processes it according to the following rules:
- Single spaces are replaced with underscores (`_`).
- Three or more consecutive spaces are replaced with a hyphen (`-`).

#### Examples

```python
from main import fix_spaces

# Example 1: No spaces
print(fix_spaces("Example"))  # Output: "Example"

# Example 2: Single space
print(fix_spaces("Example 1"))  # Output: "Example_1"

# Example 3: Leading space
print(fix_spaces(" Example 2"))  # Output: "_Example_2"

# Example 4: More than two consecutive spaces
print(fix_spaces(" Example   3"))  # Output: "_Example-3"
```

### How to Use

1. Ensure Python is installed on your system.
2. Save the provided `main.py` file in your project directory.
3. Import the `fix_spaces` function from `main.py` in your Python script.
4. Call the `fix_spaces` function with the string you wish to process.

## Documentation

For further details or updates, please refer to the source code documentation within the `main.py` file. The function is self-contained and does not require any additional libraries or dependencies.
```

This manual provides a comprehensive guide on how to use the `fix_spaces` utility, including installation instructions, usage examples, and a brief overview of its functionality.