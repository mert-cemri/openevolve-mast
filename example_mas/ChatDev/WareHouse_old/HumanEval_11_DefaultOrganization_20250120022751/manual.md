# String XOR User Manual

Welcome to the String XOR application! This software provides a simple yet efficient way to perform binary XOR operations on two input strings consisting of '1's and '0's. This manual will guide you through the installation process, introduce the main function of the software, and provide instructions on how to use it effectively.

## Main Functionality

The primary function of this software is `string_xor`, which takes two binary strings as input and returns their XOR result as a binary string. The XOR operation is performed bit by bit, where the result is '1' if the corresponding bits are different and '0' if they are the same.

### Function Signature

```python
def string_xor(a: str, b: str) -> str:
```

### Example Usage

```python
>>> string_xor('010', '110')
'100'
```

## Installation

This application does not require any external dependencies, making it straightforward to set up and use. Follow the steps below to get started:

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of the repository.

### Step 2: Navigate to the Project Directory

Change your current directory to the project directory:

```bash
cd <project-directory>
```

Replace `<project-directory>` with the actual name of the cloned directory.

### Step 3: Verify Python Environment

Ensure you have Python installed on your system. This application is compatible with Python 3.x. You can verify your Python installation by running:

```bash
python --version
```

## Usage

Once you have set up the environment, you can use the `string_xor` function as follows:

1. Open a Python interpreter or create a Python script.
2. Import the `string_xor` function from the `main.py` file.
3. Call the `string_xor` function with two binary strings of equal length as arguments.

### Example

```python
from main import string_xor

result = string_xor('1010', '1100')
print(result)  # Output: '0110'
```

## Error Handling

The `string_xor` function includes error handling to ensure both input strings are of the same length. If they are not, a `ValueError` will be raised with the message "Input strings must be of the same length."

## Conclusion

This user manual provides all the necessary information to install and use the String XOR application. If you encounter any issues or have further questions, please refer to the documentation or contact support for assistance. Enjoy using the String XOR application for your binary string operations!