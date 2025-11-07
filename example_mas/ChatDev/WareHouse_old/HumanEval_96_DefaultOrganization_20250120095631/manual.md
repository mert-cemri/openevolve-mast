manual.md

```
# Prime Number Finder

This software provides a simple utility to find all prime numbers less than a given non-negative integer. It is designed to be lightweight and efficient, requiring no external dependencies.

## Main Functions

The main function of this software is `count_up_to(n)`, which takes a non-negative integer `n` and returns a list of all prime numbers less than `n`.

### Function Details

- **`count_up_to(n)`**: 
  - **Input**: A non-negative integer `n`.
  - **Output**: A list of prime numbers less than `n`.
  - **Examples**:
    - `count_up_to(5)` returns `[2, 3]`
    - `count_up_to(11)` returns `[2, 3, 5, 7]`
    - `count_up_to(0)` returns `[]`
    - `count_up_to(20)` returns `[2, 3, 5, 7, 11, 13, 17, 19]`
    - `count_up_to(1)` returns `[]`
    - `count_up_to(18)` returns `[2, 3, 5, 7, 11, 13, 17]`

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the source code from the repository where it is hosted.

3. **Navigate to the project directory**: Use the command line to navigate to the directory containing the `main.py` file.

## Usage

To use the software, you can run the `main.py` file and call the `count_up_to` function with your desired input.

### Example Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run Python in interactive mode by typing `python` and pressing Enter.
4. Import the function by typing `from main import count_up_to`.
5. Call the function with your desired input, for example: `count_up_to(10)`.
6. View the output list of prime numbers.

This software is designed to be straightforward and efficient, providing a quick way to calculate prime numbers for educational or computational purposes.
```