# Vowels Count Software

This software provides a function to count the number of vowels in a given string. It considers 'a', 'e', 'i', 'o', 'u' as vowels, and 'y' as a vowel only if it appears at the end of the word. The software also includes a set of test cases to verify the correctness of the function.

## Main Functionality

- **vowels_count(s)**: This function takes a string `s` as input and returns the number of vowels in the string. It considers both uppercase and lowercase vowels.

## Installation

### Environment Setup

This software does not require any external dependencies, so you can run it with a standard Python installation. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Running the Software

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Test Cases**: Execute the `main.py` file to run the test cases and verify the function's correctness. You can do this by running the following command in your terminal:

   ```bash
   python main.py
   ```

   This will execute the test cases defined in the script and print any assertion errors if the function does not behave as expected.

## Usage

To use the `vowels_count` function in your own projects:

1. **Import the Function**: Copy the `vowels_count` function from the `main.py` file into your own Python script.

2. **Call the Function**: Use the function by passing a string as an argument. For example:

   ```python
   from your_script import vowels_count

   result = vowels_count("hello")
   print(result)  # Output: 2
   ```

## Testing

The `main.py` file includes a set of test cases to ensure the function works correctly. These test cases cover various scenarios, including strings with no vowels, strings with only vowels, and strings where 'y' is at the end.

To add more test cases, simply extend the `test_vowels_count` function with additional assertions.

## Conclusion

This software provides a simple yet effective way to count vowels in a string, with comprehensive test cases to ensure reliability. Feel free to modify and extend the functionality as needed for your specific use cases.