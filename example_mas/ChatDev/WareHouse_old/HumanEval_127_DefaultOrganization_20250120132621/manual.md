manual.md

```
# Interval Intersection Prime Checker

This software provides a function to determine if the length of the intersection of two given intervals is a prime number. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function provided by this software is `intersection(interval1, interval2)`. This function takes two intervals as input and returns "YES" if the length of their intersection is a prime number, and "NO" otherwise. If the intervals do not intersect, it also returns "NO".

### Function Details

- **intersection(interval1, interval2):**
  - **Input:** Two intervals, each represented as a tuple of two integers (start, end).
  - **Output:** A string "YES" or "NO" based on whether the length of the intersection is a prime number.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**
   - Clone the repository to your local machine using Git or download the ZIP file and extract it.

2. **Navigate to the Directory:**
   - Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Script:**
   - You can run the script directly using Python. No additional installation steps are required.

## How to Use

1. **Open the Terminal:**
   - Navigate to the directory containing the `main.py` file.

2. **Run the Function:**
   - You can test the function by running the Python script and calling the `intersection` function with your desired intervals.
   - Example:
     ```python
     from main import intersection
     print(intersection((1, 2), (2, 3)))  # Output: "NO"
     print(intersection((-1, 1), (0, 4)))  # Output: "NO"
     print(intersection((-3, -1), (-5, 5)))  # Output: "YES"
     ```

3. **Modify as Needed:**
   - You can modify the intervals in the function calls to test different cases.

## Documentation

For further details on how the function works, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic behind determining the intersection and checking for prime numbers.

## Support

If you encounter any issues or have questions about using this software, please feel free to reach out to our support team or check the documentation within the code for guidance.

```