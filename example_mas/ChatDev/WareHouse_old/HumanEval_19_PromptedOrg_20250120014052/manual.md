# Sort Numbers User Manual

Welcome to the Sort Numbers application! This software is designed to sort a space-delimited string of numerals from 'zero' to 'nine' in ascending order. This manual will guide you through the installation process, introduce the main function of the software, and provide instructions on how to use it.

## Main Function

The primary function of this software is `sort_numbers`, which takes a string of numerals and returns them sorted in ascending order. The valid numerals are:

- 'zero'
- 'one'
- 'two'
- 'three'
- 'four'
- 'five'
- 'six'
- 'seven'
- 'eight'
- 'nine'

### Example Usage

```python
>>> sort_numbers('three one five')
'one three five'
```

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Quick Install

1. Clone the repository or download the `main.py` file to your local machine.

2. Navigate to the directory containing `main.py`.

3. Since there are no additional dependencies required, you can directly run the script using Python.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python script and use the `sort_numbers` function as follows:

```bash
python
```

```python
from main import sort_numbers

# Example usage
result = sort_numbers('three one five')
print(result)  # Output: 'one three five'
```

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is well-documented to help you understand its usage and functionality.

Thank you for using the Sort Numbers application! If you have any questions or need further assistance, please feel free to reach out.