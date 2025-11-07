# Prime Factorization Software

This software provides a function to factorize a given integer into its prime factors. It returns a list of prime factors in the order from smallest to largest, with each factor listed the number of times it appears in the factorization.

## Main Functionality

The main function of this software is:

- **factorize(n: int) -> List[int]**: This function takes an integer `n` as input and returns a list of its prime factors. The factors are listed in ascending order, and each factor appears as many times as it divides `n`.

### Example Usage

```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```

## Installation

This software does not require any external dependencies. It is implemented in Python and can be run in any standard Python environment.

### Setting Up the Environment

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Virtual Environment (Optional but Recommended)**:
   - Navigate to your project directory.
   - Run the following command to create a virtual environment:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       .\venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```
       source venv/bin/activate
       ```

3. **Install Dependencies**: Since there are no external dependencies, you can skip this step.

## How to Use

1. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.

3. **Run the Code**: You can run the code by executing the `main.py` file in your Python environment. Use the function `factorize()` to factorize any integer as shown in the example usage.

```bash
python main.py
```

4. **Use the Function**: You can import the `factorize` function from `main.py` into your own scripts to use it as needed.

```python
from main import factorize

result = factorize(56)
print(result)  # Output: [2, 2, 2, 7]
```

## Documentation

For further documentation, please refer to the docstring provided in the `factorize` function within the `main.py` file. It includes a detailed description of the function's behavior and example usage.

This software is designed to be simple and efficient, providing a straightforward solution for prime factorization tasks.