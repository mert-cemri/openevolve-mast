manual.md

```
# Unique Digits Filter

This software provides a function to filter out numbers from a list that contain any even digits. The resulting list is sorted in increasing order.

## Main Functionality

The main function provided by this software is `unique_digits(x)`, which takes a list of positive integers and returns a sorted list of integers that do not contain any even digits.

### Example Usage

```python
from main import unique_digits

# Example usage
result1 = unique_digits([15, 33, 1422, 1])
print(result1)  # Output: [1, 15, 33]

result2 = unique_digits([152, 323, 1422, 10])
print(result2)  # Output: []
```

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Environment Setup

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Change your working directory to the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**

   Although there are no additional dependencies required for this project, it is good practice to create a virtual environment:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   Since there are no external dependencies, you can skip the installation of packages.

## How to Use

1. **Run the Script**

   You can run the script directly to see the example outputs:

   ```bash
   python main.py
   ```

   This will execute the `unique_digits` function with predefined examples and print the results.

2. **Integrate into Your Project**

   You can import the `unique_digits` function into your own Python projects and use it as needed.

## Documentation

For further details on the function and its usage, please refer to the comments within the `main.py` file. The function is designed to be straightforward and easy to integrate into larger projects.

```