Here is the user manual for the software:

---

# Remove Duplicates

A simple Python utility to remove duplicate integers from a list, retaining only those elements that occur once and maintaining their original order.

## Quick Install

This project does not require any external dependencies, so you can directly use it with a standard Python installation.

## 🤔 What is this?

This software provides a function `remove_duplicates` that processes a list of integers and removes any elements that appear more than once. The order of the elements that remain is preserved as in the original list.

### Main Function

- **remove_duplicates(numbers: List[int]) -> List[int]**

  This function takes a list of integers as input and returns a new list containing only the integers that appear exactly once in the input list.

  **Example Usage:**

  ```python
  from typing import List

  def remove_duplicates(numbers: List[int]) -> List[int]:
      """ From a list of integers, remove all elements that occur more than once.
      Keep order of elements left the same as in the input.
      >>> remove_duplicates([1, 2, 3, 2, 4])
      [1, 3, 4]
      """
      # Dictionary to count occurrences of each number
      count = {}
      # Count each number's occurrences
      for number in numbers:
          if number in count:
              count[number] += 1
          else:
              count[number] = 1
      # Collect numbers that occur only once
      result = [number for number in numbers if count[number] == 1]
      return result

  # Example usage
  unique_numbers = remove_duplicates([1, 2, 3, 2, 4])
  print(unique_numbers)  # Output: [1, 3, 4]
  ```

## 📖 Documentation

### Getting Started

1. **Installation**: No installation is required beyond having Python installed on your system.

2. **Usage**: Simply import the function `remove_duplicates` from your script and use it as demonstrated in the example above.

### How-To Examples

- **Removing Duplicates from a List**: Pass a list of integers to the `remove_duplicates` function to get a list of unique integers.

### Reference

- **Function**: `remove_duplicates(numbers: List[int]) -> List[int]`
  - **Parameters**: 
    - `numbers`: A list of integers from which duplicates need to be removed.
  - **Returns**: A list of integers that appear only once in the input list.

### Resources

For further information or support, please contact our development team at ChatDev.

---

This manual provides all necessary information to understand, install, and use the software effectively.