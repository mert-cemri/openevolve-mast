# Change Base User Manual

Welcome to the Change Base software! This tool allows you to convert a given integer from base 10 to another numerical base, with the base numbers being less than 10. This manual will guide you through the installation, usage, and main functions of the software.

## Quick Install

This software does not require any external dependencies. You only need Python installed on your system to run the code.

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

### Step 2: Clone or Download the Repository

You can clone the repository using Git or download the ZIP file from the repository page.

To clone the repository, use the following command:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of the repository.

### Step 3: Navigate to the Project Directory

Once you have the files, navigate to the project directory:

```bash
cd <project-directory>
```

Replace `<project-directory>` with the actual directory name.

## 🤔 What is this?

The Change Base software is a simple Python script that converts a given integer from base 10 to another specified base. The base must be between 2 and 9, inclusive. This tool is useful for educational purposes, software development, and understanding numerical base conversions.

## Main Function

The main function of this software is `change_base(x: int, base: int) -> str`. It takes two parameters:

- `x`: The integer you want to convert.
- `base`: The base to which you want to convert the integer. The base must be between 2 and 9.

### Example Usage

Here are some examples of how to use the `change_base` function:

```python
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `main.py` file.
3. Run the Python script using the following command:

```bash
python main.py
```

4. You can modify the `main.py` file to include your own test cases or use the function in your own Python scripts.

## 📖 Documentation

For further information or assistance, please refer to the comments within the `main.py` file. The code is documented to help you understand the logic and flow of the conversion process.

Thank you for using the Change Base software! If you have any questions or need further support, please feel free to reach out.