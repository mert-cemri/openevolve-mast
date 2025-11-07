# Rescale to Unit

This software provides a simple utility function to rescale a list of numbers to a unit scale, where the smallest number becomes 0 and the largest becomes 1. This can be useful for normalizing data for various applications such as data analysis, machine learning, and more.

## Quick Install

No external dependencies are required for this software. It uses only the Python standard library. Ensure you have Python installed on your system.

## 🤔 What is this?

The `rescale_to_unit` function takes a list of floating-point numbers and applies a linear transformation to rescale the numbers. The transformation ensures that the smallest number in the list becomes 0 and the largest becomes 1, with all other numbers proportionally adjusted between these two values.

### Main Function

- **`rescale_to_unit(numbers: List[float]) -> List[float]`**

  - **Parameters:**
    - `numbers`: A list of floating-point numbers with at least two elements.
  
  - **Returns:**
    - A list of floating-point numbers rescaled to the unit interval [0, 1].

  - **Example:**
    ```python
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    ```

## 📖 How to Use

1. **Ensure Python is Installed:**

   Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Create a Python Script:**

   Create a Python script file, e.g., `main.py`, and include the following code:

   ```python
   from typing import List

   def rescale_to_unit(numbers: List[float]) -> List[float]:
       min_value = min(numbers)
       max_value = max(numbers)
       range_value = max_value - min_value
       return [(num - min_value) / range_value for num in numbers]
   
   # Example usage
   numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   rescaled_numbers = rescale_to_unit(numbers)
   print(rescaled_numbers)
   ```

3. **Run the Script:**

   Open a terminal or command prompt, navigate to the directory containing your script, and run:

   ```bash
   python main.py
   ```

   This will output the rescaled list:

   ```
   [0.0, 0.25, 0.5, 0.75, 1.0]
   ```

## Additional Information

- **No External Libraries:** This function does not require any external Python libraries, making it lightweight and easy to integrate into existing projects.
- **Use Cases:** This function is particularly useful in data preprocessing steps where normalization of data is required.

Feel free to modify and integrate this function into your projects as needed!