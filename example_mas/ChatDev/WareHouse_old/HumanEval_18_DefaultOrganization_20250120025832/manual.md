manual.md

```
# How Many Times

A simple Python application to find how many times a given substring can be found in the original string, including overlapping cases.

## Overview

The `how_many_times` function is designed to count the occurrences of a specified substring within a given string, considering overlapping instances. This can be particularly useful in text analysis and pattern recognition tasks.

## Main Functionality

- **how_many_times(string: str, substring: str) -> int**: This function takes two parameters:
  - `string`: The original string in which to search for the substring.
  - `substring`: The substring to search for within the original string.
  
  The function returns an integer representing the number of times the substring is found in the string, including overlapping occurrences.

### Example Usage

```python
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
```

## Installation

This application does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Step-by-Step Installation

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the source code by cloning the repository or downloading it as a ZIP file.

3. **Navigate to the Project Directory**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

4. **Run the Application**: Execute the Python script using the command:
   ```bash
   python main.py
   ```

## Usage

To use the `how_many_times` function, you can either call it directly within the script or import it into another Python script. Here’s how you can use it in a Python script:

```python
from main import how_many_times

result = how_many_times('your_string_here', 'your_substring_here')
print(f"The substring appears {result} times.")
```

## Documentation

For further details and examples, please refer to the inline documentation within the `main.py` file. The function is well-documented with examples to guide you through its usage.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to assist you with any challenges you may encounter while using the application.
```
