# DigitSum Function

This software provides a simple utility function to calculate the sum of ASCII values of uppercase characters in a given string. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The primary function of this software is:

- **digitSum(s):** This function takes a string `s` as input and returns the sum of the ASCII values of all uppercase characters in the string. If there are no uppercase characters, it returns 0.

### Example Usage

```python
print(digitSum(""))          # Output: 0
print(digitSum("abAB"))      # Output: 131
print(digitSum("abcCd"))     # Output: 67
print(digitSum("helloE"))    # Output: 69
print(digitSum("woArBld"))   # Output: 131
print(digitSum("aAaaaXa"))   # Output: 153
```

## Installation

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change your working directory to the project folder:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies:**

   This project does not require any external dependencies. However, ensure that your Python environment is set up correctly.

   If you are using a virtual environment, you can create and activate it using:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Run the Code:**

   You can run the code directly using Python:

   ```bash
   python main.py
   ```

## How to Use

To use the `digitSum` function, simply import it into your Python script and call it with the desired string as an argument. The function will return the sum of ASCII values of uppercase characters in the string.

### Example

```python
from main import digitSum

result = digitSum("HelloWorld")
print("The sum of ASCII values of uppercase characters is:", result)
```

## Documentation

For further details and documentation, please refer to the comments within the `main.py` file. The function is straightforward and self-explanatory, designed to be easily integrated into other projects or used as a standalone utility.

## Support

For any issues or questions, please contact the development team at support@chatdev.com. We are here to help you with any queries related to the software.