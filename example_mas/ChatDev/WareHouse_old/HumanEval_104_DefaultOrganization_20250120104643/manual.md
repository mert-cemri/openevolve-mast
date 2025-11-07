# Unique Digits Software

This software provides a function to filter and sort a list of positive integers, returning only those numbers that do not contain any even digits.

## Main Functionality

The main function of this software is `unique_digits`, which takes a list of positive integers and returns a sorted list of numbers that do not have any even digits. 

### Example Usage

```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

## Installation

To use this software, you need to have Python installed on your system. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the project folder.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Although there are no additional dependencies listed in the `requirements.txt` file, ensure your Python environment is set up correctly.

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is empty, you can skip this step.

## Usage

To use the `unique_digits` function, you can import it into your Python script or use it directly in an interactive Python session.

### Example

```python
from main import unique_digits

# Example list of numbers
numbers = [15, 33, 1422, 1]

# Get numbers without even digits
result = unique_digits(numbers)

# Output the result
print(result)  # Output: [1, 15, 33]
```

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is straightforward and designed to be used in any Python environment without additional setup.

## Support

If you encounter any issues or have questions about using this software, please contact our support team at support@chatdev.com. We are here to help you with any inquiries or technical support you may need.