# Exchange Function User Manual

Welcome to the user manual for the Exchange Function, a simple Python utility designed to determine if it's possible to make all elements of one list even by exchanging elements with another list.

## Overview

The Exchange Function is a straightforward Python script that helps users determine whether it's possible to transform a list (`lst1`) into a list of only even numbers by exchanging elements with another list (`lst2`). The function returns "YES" if the transformation is possible and "NO" otherwise.

## Main Functionality

- **Function Name:** `exchange(lst1, lst2)`
- **Purpose:** To check if all elements in `lst1` can be made even by exchanging elements with `lst2`.
- **Input:** Two non-empty lists of integers, `lst1` and `lst2`.
- **Output:** A string, either "YES" or "NO".

## Installation

This project does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Step-by-Step Installation Guide

1. **Install Python:**
   - Download and install Python from the official website: [python.org](https://www.python.org/downloads/).
   - Follow the installation instructions for your operating system.

2. **Clone or Download the Project:**
   - Clone the repository using Git:
     ```bash
     git clone <repository-url>
     ```
   - Or download the project as a ZIP file and extract it to your desired location.

3. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the project is located.

## Usage

To use the Exchange Function, follow these steps:

1. **Open the Terminal or Command Prompt:**
   - Navigate to the directory containing the `main.py` file.

2. **Run the Script:**
   - Execute the script using Python:
     ```bash
     python main.py
     ```

3. **Call the Function:**
   - Within the script, you can call the `exchange` function with your desired lists:
     ```python
     result = exchange([1, 2, 3, 4], [1, 2, 3, 4])
     print(result)  # Output: "YES"
     ```

4. **Interpret the Result:**
   - The function will return "YES" if it's possible to make all elements of `lst1` even by exchanging elements with `lst2`. Otherwise, it will return "NO".

## Example

Here's an example of how you might use the function in a Python script:

```python
# Example usage of the exchange function
def main():
    lst1 = [1, 2, 3, 4]
    lst2 = [1, 2, 3, 4]
    result = exchange(lst1, lst2)
    print(f"Can lst1 be made all even? {result}")

if __name__ == "__main__":
    main()
```

## Conclusion

The Exchange Function is a simple yet effective tool for determining the possibility of transforming a list into even numbers through element exchange. With no external dependencies, it is easy to set up and use in any Python environment. Enjoy using the function for your list transformation needs!