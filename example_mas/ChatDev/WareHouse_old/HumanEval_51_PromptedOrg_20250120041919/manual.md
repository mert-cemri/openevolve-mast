```markdown
# Remove Vowels Function

This software provides a simple Python function to remove vowels from a given string. The function is designed to handle both uppercase and lowercase vowels and can process multi-line strings.

## Main Functionality

The primary function of this software is:

- **remove_vowels(text):** This function takes a string as input and returns a new string with all vowels (both uppercase and lowercase) removed. It handles multi-line strings and retains all non-vowel characters, including special characters and spaces.

### Example Usage

```python
from main import remove_vowels

# Example usage
print(remove_vowels('abcdef'))  # Output: 'bcdf'
print(remove_vowels('aaBAA'))   # Output: 'B'
print(remove_vowels('abcdef\nghijklm'))  # Output: 'bcdf\nghjklm'
```

## Installation

This project does not require any external dependencies, so you can use it directly with a standard Python installation.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Run the Code:**

   You can run the code directly using Python:

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function:**

   Import the `remove_vowels` function from the `main.py` file in your Python script:

   ```python
   from main import remove_vowels
   ```

2. **Call the Function:**

   Pass a string to the `remove_vowels` function to get a new string with vowels removed:

   ```python
   result = remove_vowels("Your input string here")
   print(result)
   ```

## Documentation

The function is documented with examples in the docstring. You can view the examples by opening the `main.py` file and looking at the `remove_vowels` function.

For any further questions or support, please contact our support team.

```
```