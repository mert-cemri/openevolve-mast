manual.md

```
# Prime Factorization Software

This software provides a simple and efficient way to factorize a given integer into its prime factors. It is designed to return a list of prime factors in ascending order, with each factor appearing as many times as it divides the number.

## Main Functionality

The main functionality of this software is encapsulated in the `factorize` function, which takes an integer as input and returns a list of its prime factors.

### Function: `factorize`

- **Input:** An integer `n`.
- **Output:** A list of integers representing the prime factors of `n`.

#### Example Usage

```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**
   - You can clone the repository from your version control system.

2. **Navigate to the Project Directory:**
   - Open your terminal or command prompt.
   - Navigate to the directory where the `main.py` file is located.

3. **Run the Script:**
   - You can run the script directly using Python.
   - Example command:
     ```
     python main.py
     ```

## How to Use

1. **Import the Function:**
   - In your Python script or interactive shell, import the `factorize` function from `main.py`.

   ```python
   from main import factorize
   ```

2. **Call the Function:**
   - Pass the integer you want to factorize as an argument to the `factorize` function.

   ```python
   result = factorize(56)
   print(result)  # Output: [2, 2, 2, 7]
   ```

3. **Interpret the Results:**
   - The function will return a list of prime factors. Each factor will appear as many times as it divides the input number.

## Additional Information

- **No External Libraries Required:** This software is built using only Python's standard library, ensuring compatibility and ease of use.
- **Efficient Algorithm:** The algorithm efficiently finds and lists all prime factors of a given integer.

For any further questions or support, please contact our support team.
```
