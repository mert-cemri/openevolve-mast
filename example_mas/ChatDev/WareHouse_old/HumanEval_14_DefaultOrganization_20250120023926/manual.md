# All Prefixes Software

This software provides a simple utility function to generate all prefixes of a given string. It is designed to be lightweight and easy to use, with no external dependencies required.

## Main Function

The core functionality of this software is provided by the `all_prefixes` function. This function takes a single input string and returns a list of all its prefixes, ordered from shortest to longest.

### Function Signature

```python
def all_prefixes(string: str) -> List[str]:
```

### Example Usage

```python
>>> all_prefixes('abc')
['a', 'ab', 'abc']
```

## Installation

Since this project does not require any external dependencies, setting up the environment is straightforward. You only need to have Python installed on your system.

### Prerequisites

- Python 3.x

### Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Run the Code**

   You can directly run the `main.py` file to test the function:

   ```bash
   python main.py
   ```

## How to Use

To use the `all_prefixes` function in your own projects, you can import it from the `main.py` file. Here's an example of how to do that:

```python
from main import all_prefixes

# Example usage
result = all_prefixes('example')
print(result)  # Output: ['e', 'ex', 'exa', 'exam', 'examp', 'exampl', 'example']
```

## Documentation

For further information and examples, please refer to the inline documentation provided in the `main.py` file. The function is designed to be intuitive and easy to integrate into your own projects.

## Support

If you encounter any issues or have questions about using this software, please feel free to reach out through the project's issue tracker on the repository page.

---

This manual provides all the necessary information to get started with the All Prefixes software. Enjoy using the utility and feel free to contribute to its development!