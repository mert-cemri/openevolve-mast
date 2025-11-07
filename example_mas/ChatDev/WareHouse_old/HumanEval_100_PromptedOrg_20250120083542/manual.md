# Stone Pile Builder

The Stone Pile Builder is a simple Python application that allows users to create a pile of stones with a specified number of levels. Each level of the pile contains a specific number of stones, determined by whether the initial number of stones is odd or even.

## Main Functionality

The main function of this application is `make_a_pile(n)`, which takes a positive integer `n` as input and returns a list representing the number of stones in each level of the pile. The pile has `n` levels, and the number of stones in each level is determined as follows:

- The first level has `n` stones.
- The number of stones in the next level is:
  - The next odd number if `n` is odd.
  - The next even number if `n` is even.

### Example

```python
>>> make_a_pile(3)
[3, 5, 7]
```

In this example, the pile has 3 levels. The first level has 3 stones, the second level has 5 stones, and the third level has 7 stones.

## Installation

This application does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Ensure Python is installed** on your system. You can download Python from the [official website](https://www.python.org/downloads/).

3. **No additional packages are required**, so you can directly run the script.

## How to Use

1. **Open a terminal or command prompt** on your computer.

2. **Navigate to the directory** where the `main.py` file is located.

3. **Run the script** using Python by executing the following command:

   ```bash
   python main.py
   ```

4. **Call the `make_a_pile` function** within the script or an interactive Python session to generate a pile of stones. For example:

   ```python
   from main import make_a_pile
   print(make_a_pile(5))
   ```

   This will output the list of stones in each level of the pile.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is well-documented to help you understand how it works and how to modify it if necessary.

Feel free to reach out for support if you encounter any issues or have questions about using the Stone Pile Builder.