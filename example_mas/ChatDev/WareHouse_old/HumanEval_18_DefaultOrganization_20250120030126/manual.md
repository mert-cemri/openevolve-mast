# User Manual for Overlapping Substring Counter

This manual provides detailed instructions on how to use the Overlapping Substring Counter software, which is designed to count the number of overlapping occurrences of a given substring within a string.

## Introduction

The Overlapping Substring Counter is a simple Python application that allows users to determine how many times a specific substring appears in a given string, including overlapping occurrences. This can be useful in various text processing and analysis tasks.

### Main Function

The core function of this software is:

- `how_many_times(string: str, substring: str) -> int`: This function takes two arguments, `string` and `substring`, and returns the number of times the `substring` appears in the `string`, counting overlapping occurrences.

#### Example Usage

```python
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
```

## Installation

To use the Overlapping Substring Counter, you need to have Python installed on your system. The software does not require any additional dependencies, so you can directly run the Python script.

### Step-by-Step Installation Guide

1. **Install Python**: Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Download the Script**: Obtain the `main.py` file containing the function definition.

3. **Run the Script**: You can execute the script using a Python interpreter. Open a terminal or command prompt, navigate to the directory containing `main.py`, and run the following command:

   ```bash
   python main.py
   ```

## How to Use

1. **Open a Python Environment**: You can use any Python environment such as IDLE, Jupyter Notebook, or a simple terminal.

2. **Import the Function**: If you are using the function in another script, make sure to import it:

   ```python
   from main import how_many_times
   ```

3. **Call the Function**: Use the `how_many_times` function by passing the desired string and substring as arguments:

   ```python
   result = how_many_times('your_string_here', 'your_substring_here')
   print(result)
   ```

4. **Interpret the Result**: The function will return an integer indicating the number of overlapping occurrences of the substring in the string.

## Conclusion

The Overlapping Substring Counter is a straightforward tool for counting overlapping substrings in a string. With no additional dependencies required, it is easy to set up and use in any Python environment. Whether for educational purposes or practical applications, this tool provides a simple solution for substring counting tasks.