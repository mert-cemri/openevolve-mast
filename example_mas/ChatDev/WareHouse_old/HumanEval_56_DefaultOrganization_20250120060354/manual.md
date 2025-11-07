# Correct Bracketing

This software provides a simple utility function to check if a string of brackets ("<" and ">") is correctly balanced. It ensures that every opening bracket has a corresponding closing bracket.

## Main Functionality

The main function provided by this software is `correct_bracketing`. This function takes a string of brackets as input and returns a boolean indicating whether the brackets are correctly balanced.

### Function Signature

```python
def correct_bracketing(brackets: str) -> bool:
```

### Example Usage

```python
>>> correct_bracketing("<")
False
>>> correct_bracketing("<>")
True
>>> correct_bracketing("<<><>>")
True
>>> correct_bracketing("><<>")
False
```

## Installation

This software does not require any external dependencies, making it straightforward to use. You only need to have Python installed on your system.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**: Clone the repository to your local machine using the following command:

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Directory**: Change into the directory where the code is located:

    ```bash
    cd <repository-directory>
    ```

3. **Run the Code**: You can directly run the `main.py` file to test the function:

    ```bash
    python main.py
    ```

## How to Use

1. **Import the Function**: If you want to use the `correct_bracketing` function in your own project, you can import it as follows:

    ```python
    from main import correct_bracketing
    ```

2. **Call the Function**: Pass a string of brackets to the function to check if they are correctly balanced:

    ```python
    result = correct_bracketing("<<><>>")
    print(result)  # Output: True
    ```

## Documentation

For further details on how the function works, you can refer to the docstring provided in the `main.py` file. The docstring includes a description of the function, its parameters, and example usage.

This software is designed to be simple and efficient, providing a quick way to verify the correctness of bracket sequences in strings.