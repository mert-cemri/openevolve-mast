# Odd Count Software

This software provides a function to count the number of odd digits in each string of a list and returns a formatted string for each input string. It is designed to work with lists of strings where each string consists solely of digits.

## Main Functionality

The main function of this software is `odd_count(lst)`, which takes a list of strings as input. Each string should consist only of digits. The function returns a list of strings, where each string describes the number of odd digits found in the corresponding input string.

### Example Usage

```python
# Example usage
if __name__ == "__main__":
    print(odd_count(['1234567']))  
    # Output: ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    
    print(odd_count(['3', "11111111"]))  
    # Output: ["the number of odd elements 1n the str1ng 1 of the 1nput.", 
    #          "the number of odd elements 8n the str8ng 8 of the 8nput."]
```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You can run the code in any Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py` and run the script using Python:

   ```bash
   python main.py
   ```

## How to Use

1. **Prepare Your Input:** Create a list of strings, where each string contains only digits.

2. **Call the Function:** Use the `odd_count(lst)` function, passing your list as the argument.

3. **Receive Output:** The function will return a list of formatted strings, each indicating the number of odd digits in the corresponding input string.

## Documentation

For further details on the implementation and examples, please refer to the comments within the `main.py` file. The code is self-explanatory and includes example usage to demonstrate its functionality.

This software is designed to be simple and efficient, with no additional setup required beyond having Python installed. Enjoy using the Odd Count Software to analyze your digit strings!