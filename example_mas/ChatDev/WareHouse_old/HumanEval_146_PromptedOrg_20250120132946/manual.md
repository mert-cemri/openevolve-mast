# SpecialFilter User Manual

Welcome to the SpecialFilter software! This tool is designed to filter numbers based on specific criteria: numbers greater than 10 with both first and last digits being odd. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it.

## Main Functionality

The primary function of this software is `specialFilter`, which processes an array of numbers and returns the count of numbers that meet the following criteria:
- The number is greater than 10.
- Both the first and last digits of the number are odd (1, 3, 5, 7, 9).

### Example Usage

- `specialFilter([15, -73, 14, -15])` returns `1`.
- `specialFilter([33, -2, -3, 45, 21, 109])` returns `2`.

## Installation

### Environment Setup

This project does not require any external dependencies, making it straightforward to set up. You only need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change into the project directory:
   ```bash
   cd <project-directory>
   ```

4. **Run the Script**: You can run the script directly using Python:
   ```bash
   python main.py
   ```

## How to Use

To use the `specialFilter` function, follow these steps:

1. **Open the `main.py` File**: Locate the `main.py` file in your project directory.

2. **Call the `specialFilter` Function**: You can call the function with an array of numbers as an argument. For example:
   ```python
   result = specialFilter([15, -73, 14, -15])
   print(result)  # Output will be 1
   ```

3. **Modify Input as Needed**: You can change the input array to test different sets of numbers.

## Conclusion

The SpecialFilter software is a simple yet effective tool for filtering numbers based on specific criteria. With no external dependencies, it is easy to set up and use. We hope this manual helps you get started with using the software efficiently. If you have any questions or need further assistance, please feel free to reach out.