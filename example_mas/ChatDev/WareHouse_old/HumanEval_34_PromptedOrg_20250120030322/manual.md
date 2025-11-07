# Unique Function

This software provides a simple utility function to return sorted unique elements from a list. It is implemented in Python and does not require any external dependencies.

## Quick Install

Since there are no external dependencies required for this software, you can directly use it in any Python environment without additional installation steps.

## 🤔 What is this?

The `unique` function is a utility that takes a list of elements and returns a new list containing only the unique elements from the original list, sorted in ascending order. This can be particularly useful for data processing tasks where duplicate entries need to be removed and the data needs to be organized.

### Main Function

- **unique(l: list) -> list**: This function takes a list `l` as input and returns a list of unique elements sorted in ascending order.

  **Example Usage:**

  ```python
  from main import unique

  result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
  print(result)  # Output: [0, 2, 3, 5, 9, 123]
  ```

## 📖 How to Use

1. **Prepare Your Environment:**
   - Ensure you have Python installed on your system. This function is compatible with Python 3.x.

2. **Using the Function:**
   - Save the provided code in a file named `main.py`.
   - Import the `unique` function from `main.py` in your Python script or interactive session.
   - Call the `unique` function with a list of elements you wish to process.

3. **Example:**

   ```python
   # Save this code in main.py
   def unique(l: list):
       """Return sorted unique elements in a list
       >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
       [0, 2, 3, 5, 9, 123]
       """
       return sorted(set(l))

   # In your script or interactive session
   from main import unique

   # Example usage
   numbers = [5, 3, 5, 2, 3, 3, 9, 0, 123]
   unique_numbers = unique(numbers)
   print(unique_numbers)  # Output: [0, 2, 3, 5, 9, 123]
   ```

## Additional Information

- **Documentation:** The function is self-documented with a docstring that includes an example of its usage.
- **No External Libraries:** This function uses only Python's built-in capabilities, so no additional libraries are required.

Feel free to integrate this utility into your projects where you need to process lists to obtain sorted unique elements.