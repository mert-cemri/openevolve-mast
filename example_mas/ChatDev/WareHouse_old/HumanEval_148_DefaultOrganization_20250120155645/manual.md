# Planet Orbit Finder

This software provides a function to determine the planets located between two given planets in the solar system. It is a simple Python application that can be used to find the sequence of planets between any two specified planets.

## Main Functionality

The main functionality of this software is encapsulated in the `bf` function. This function takes two planet names as input and returns a tuple containing all planets whose orbits are located between the orbits of the two specified planets, sorted by their proximity to the sun.

### Function: `bf`

- **Input**: Two strings representing the names of planets (`planet1` and `planet2`).
- **Output**: A tuple of planet names that are located between the orbits of `planet1` and `planet2`. If either of the input planet names is incorrect, the function returns an empty tuple.

### Example Usage

```python
bf("Jupiter", "Neptune")  # Returns: ("Saturn", "Uranus")
bf("Earth", "Mercury")    # Returns: ("Venus")
bf("Mercury", "Uranus")   # Returns: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py`.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python interpreter and import the function:

   ```bash
   python
   ```

   ```python
   from main import bf
   ```

4. Use the `bf` function by passing the names of two planets as arguments:

   ```python
   result = bf("Earth", "Mars")
   print(result)  # Output: ()
   ```

5. The function will return a tuple of planet names that are located between the specified planets.

## Documentation

For further details on the implementation and usage, please refer to the comments within the `main.py` file. The code is documented to provide insights into the logic and flow of the function.

This software is designed to be simple and straightforward, providing a quick way to determine the sequence of planets between any two given planets in our solar system.