# Sort Numbers User Manual

Welcome to the Sort Numbers application! This software is designed to sort a space-delimited string of numerals from 'zero' to 'nine' in ascending order. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it.

## Main Functions

The primary function of this software is `sort_numbers`, which takes a string of numeral words and returns them sorted in ascending order. The valid numeral words are:

- zero
- one
- two
- three
- four
- five
- six
- seven
- eight
- nine

### Example

```python
>>> sort_numbers('three one five')
'one three five'
```

## Installation

### Prerequisites

- Python 3.x

### Quick Install

Since there are no external dependencies required for this project, you can simply clone the repository and run the script.

1. **Clone the Repository**

   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned directory.

3. **Run the Application**

   You can run the application using Python:

   ```bash
   python main.py
   ```

   This will execute the example usage of the `sort_numbers` function.

## How to Use

To use the `sort_numbers` function, you can either run the `main.py` script directly or import the function into another Python script.

### Running Directly

Simply execute the `main.py` script to see the example usage:

```bash
python main.py
```

### Importing into Another Script

You can import the `sort_numbers` function into your own Python script:

```python
from main import sort_numbers

result = sort_numbers('three one five')
print(result)  # Output: 'one three five'
```

## Conclusion

This user manual provides a comprehensive guide to installing and using the Sort Numbers application. If you have any questions or encounter any issues, please feel free to reach out for support. Enjoy sorting your numeral strings with ease!