# Remove Duplicates

A simple Python module to remove duplicate integers from a list, keeping only the elements that occur once and maintaining their original order.

## Main Function

The main function provided by this module is `remove_duplicates`, which takes a list of integers as input and returns a new list with all elements that occur more than once removed.

### Function Signature

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
```

### Example Usage

```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
```

## Installation

This module does not require any external dependencies, so you can use it directly without installing additional packages.

### Quick Start

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

   You can run the code using Python. Ensure you have Python installed on your machine.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**

   To use the `remove_duplicates` function in your own Python script, import it from the module:

   ```python
   from main import remove_duplicates
   ```

2. **Call the Function**

   Pass a list of integers to the function and receive a list with duplicates removed:

   ```python
   unique_numbers = remove_duplicates([1, 2, 3, 2, 4])
   print(unique_numbers)  # Output: [1, 3, 4]
   ```

## Documentation

This module is designed to be straightforward and easy to use. The function `remove_duplicates` efficiently removes duplicate integers from a list, ensuring that only unique elements remain in their original order.

For further information or assistance, please refer to the source code or contact the development team.