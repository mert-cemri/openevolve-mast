# Prime Length Words Extractor

This software module is designed to extract words from a given sentence whose lengths are prime numbers. It is implemented in Python and does not require any external dependencies.

## Main Functions

### `is_prime(n)`

- **Purpose**: Checks if a given number `n` is a prime number.
- **Parameters**: 
  - `n` (int): The number to check for primality.
- **Returns**: 
  - `True` if `n` is a prime number.
  - `False` otherwise.

### `words_in_sentence(sentence)`

- **Purpose**: Extracts words from a sentence whose lengths are prime numbers.
- **Parameters**: 
  - `sentence` (str): A string representing a sentence.
- **Returns**: 
  - A string containing words from the original sentence that have prime lengths, maintaining their original order.

## Installation

This software does not require any external libraries or dependencies. It is implemented in pure Python. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository**: 
   - You can clone the repository or download the `main.py` file to your local machine.

2. **Run the Code**:
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the Python script using the command:
     ```bash
     python main.py
     ```
   - You can modify the `sentence` variable within the script to test different sentences.

3. **Example Usage**:
   - If you input the sentence `"This is a test"`, the output will be `"is"`.
   - For the sentence `"lets go for swimming"`, the output will be `"go for"`.

## Additional Information

- **Constraints**:
  - The length of the sentence should be between 1 and 100 characters.
  - The sentence should contain only letters and spaces.

This module is a simple yet effective tool for filtering words based on their lengths being prime numbers, which can be useful in various text processing applications.