# Car Race Collision Software

This software provides a simple function to calculate the number of collisions between two sets of cars moving in opposite directions on an infinitely long straight road. Each set consists of `n` cars, with one set moving left to right and the other moving right to left. The function assumes that all cars move at the same speed and continue moving after collisions.

## Main Functionality

The main function provided by this software is:

- `car_race_collision(n: int) -> int`: This function calculates the number of collisions between two sets of cars. Given `n`, the number of cars in each set, the function returns the total number of collisions. Since each car from the left-to-right set will collide with exactly one car from the right-to-left set, the number of collisions is equal to `n`.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: Download or clone the repository containing the `main.py` file.

3. **Navigate to the directory**: Open a terminal or command prompt and navigate to the directory where `main.py` is located.

## How to Use

1. **Open the Python file**: Open `main.py` in your preferred code editor.

2. **Call the function**: Use the `car_race_collision` function by passing the number of cars in each set as an argument. For example:

   ```python
   from main import car_race_collision

   number_of_cars = 5
   collisions = car_race_collision(number_of_cars)
   print(f"Number of collisions: {collisions}")
   ```

3. **Run the script**: Execute the script in your terminal or command prompt by running:

   ```bash
   python main.py
   ```

   This will output the number of collisions based on the input provided.

## Example

Here's a simple example to demonstrate the usage of the function:

```python
from main import car_race_collision

# Define the number of cars in each set
n = 10

# Calculate the number of collisions
collisions = car_race_collision(n)

# Output the result
print(f"Number of collisions: {collisions}")
```

This example will output:

```
Number of collisions: 10
```

## Conclusion

This software provides a straightforward solution to calculate the number of collisions between two sets of cars moving in opposite directions. With no external dependencies, it is easy to set up and use. Simply define the number of cars in each set, call the function, and retrieve the number of collisions.