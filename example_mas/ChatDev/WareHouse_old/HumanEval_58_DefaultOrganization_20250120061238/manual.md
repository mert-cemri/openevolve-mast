# Common Elements Finder

This software module provides a simple utility to find sorted unique common elements from two lists. It is implemented in Python and is designed to be straightforward and efficient.

## Main Functionality

The primary function of this module is `common(l1: list, l2: list)`, which takes two lists as input and returns a sorted list of unique elements that are common to both lists.

### Example Usage

```python
from main import common

# Example 1
result1 = common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
print(result1)  # Output: [1, 5, 653]

# Example 2
result2 = common([5, 3, 2, 8], [3, 2])
print(result2)  # Output: [2, 3]
```

## Installation

### Prerequisites

- Python 3.x installed on your system.

### Installation Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**

   Although there are no external dependencies for this module, it is always a good practice to create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Then, install any necessary dependencies (if any are added in the future):

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Import the Function**

   Import the `common` function from the `main.py` file in your Python script.

2. **Call the Function**

   Pass two lists as arguments to the `common` function to get the sorted unique common elements.

3. **View the Results**

   The function will return a list of sorted unique common elements, which you can print or use in further processing.

## Documentation

For more detailed documentation, refer to the docstring provided in the `main.py` file. It includes examples and a brief description of the function's purpose and usage.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the repository. We are here to assist you in making the most out of this utility.

---

This manual provides a comprehensive guide to using the Common Elements Finder module. Follow the instructions carefully to set up and utilize the software effectively.