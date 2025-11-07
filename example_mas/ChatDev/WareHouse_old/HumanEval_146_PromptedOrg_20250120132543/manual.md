# SpecialFilter User Manual

Welcome to the SpecialFilter software! This tool is designed to filter numbers based on specific criteria, providing a simple yet powerful way to analyze numerical data.

## Main Functionality

The core function of this software is `specialFilter`, which processes an array of numbers and returns the count of elements that meet the following criteria:
- The number is greater than 10.
- Both the first and last digits of the number are odd (1, 3, 5, 7, 9).

### Example Usage

- `specialFilter([15, -73, 14, -15])` returns `1`
- `specialFilter([33, -2, -3, 45, 21, 109])` returns `2`

## Installation

### Environment Setup

This software is implemented in Python and does not require any external dependencies. To get started, ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**: 
   - If the code is hosted in a repository, clone it using:
     ```bash
     git clone <repository-url>
     ```
   - Navigate to the project directory:
     ```bash
     cd <project-directory>
     ```

2. **Install Python**:
   - Ensure Python is installed on your system. You can verify the installation by running:
     ```bash
     python --version
     ```

3. **Install Dependencies**:
   - No external dependencies are required for this project. However, if you plan to use a virtual environment, you can set it up using:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

## How to Use

1. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `main.py`.
   - Execute the script using Python:
     ```bash
     python main.py
     ```

2. **Using the Function**:
   - You can directly call the `specialFilter` function within your Python environment or script by importing it from `main.py`:
     ```python
     from main import specialFilter

     result = specialFilter([33, -2, -3, 45, 21, 109])
     print(result)  # Output will be 2
     ```

## Documentation

For further information and detailed documentation, please refer to the comments within the `main.py` file. The code is well-documented to provide clarity on the logic and functionality of the `specialFilter` function.

Thank you for using SpecialFilter! We hope this tool meets your data filtering needs effectively. If you have any questions or require support, please feel free to reach out.