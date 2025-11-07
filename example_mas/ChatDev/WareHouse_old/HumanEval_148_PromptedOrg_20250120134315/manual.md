# Planetary Orbit Finder

This software provides a function to determine the planets located between two given planets in our solar system. It is a simple Python application that can be used to understand the relative positions of planets based on their proximity to the Sun.

## Main Functionality

The main function provided by this software is `bf(planet1, planet2)`. This function takes two planet names as input and returns a tuple of planet names that are located between the orbits of the two specified planets, sorted by their proximity to the Sun. If either of the input planet names is incorrect, the function returns an empty tuple.

### Examples

- `bf("Jupiter", "Neptune")` returns `("Saturn", "Uranus")`
- `bf("Earth", "Mercury")` returns `("Venus")`
- `bf("Mercury", "Uranus")` returns `("Venus", "Earth", "Mars", "Jupiter", "Saturn")`

## Installation

This software does not require any external dependencies. It is a standalone Python script that can be run in any Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are required as there are no external dependencies.

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

4. Use the `bf` function by passing the names of two planets as strings:

   ```python
   result = bf("Jupiter", "Neptune")
   print(result)  # Output: ("Saturn", "Uranus")
   ```

5. Experiment with different planet combinations to see the planets located between them.

## Documentation

For further information or questions, please refer to the comments within the `main.py` file, which provide additional context and examples for using the `bf` function.

This software is designed to be simple and educational, providing insights into the order of planets in our solar system. Enjoy exploring the cosmos!