# Histogram Software User Manual

Welcome to the Histogram Software User Manual. This document provides a comprehensive guide on how to use the software, including its main functions, installation instructions, and usage examples.

## Overview

The Histogram software is a Python application designed to analyze a string of space-separated lowercase letters and return a dictionary of the letters with the most repetitions, along with their corresponding counts. If multiple letters have the same highest occurrence, all of them are returned.

### Main Function

- **histogram(test: str) -> dict**: This function takes a string input and returns a dictionary containing the letters with the highest repetition count. If the input string is empty, it returns an empty dictionary.

### Examples

- `histogram('a b c')` returns `{'a': 1, 'b': 1, 'c': 1}`
- `histogram('a b b a')` returns `{'a': 2, 'b': 2}`
- `histogram('a b c a b')` returns `{'a': 2, 'b': 2}`
- `histogram('b b b b a')` returns `{'b': 4}`
- `histogram('')` returns `{}`

## Installation

The Histogram software does not require any external dependencies, making it straightforward to set up and use. Follow the steps below to install and run the software:

### Prerequisites

- Ensure you have Python installed on your system. The software is compatible with Python 3.x versions.

### Installation Steps

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Software**: You can run the software directly using Python. No additional installation steps are required.

## Usage

To use the Histogram software, follow these steps:

1. **Open a Terminal**: Open a terminal or command prompt on your computer.

2. **Navigate to the Directory**: Use the `cd` command to navigate to the directory containing the `main.py` file.

3. **Run the Script**: Execute the script by running the following command:
   ```bash
   python main.py
   ```

4. **Use the Function**: You can call the `histogram` function within the script or import it into another Python script to use it programmatically.

## Conclusion

The Histogram software is a simple yet powerful tool for analyzing letter frequency in a string. With no external dependencies, it is easy to set up and use. We hope this user manual helps you get started with the software. If you have any questions or need further assistance, please feel free to reach out.