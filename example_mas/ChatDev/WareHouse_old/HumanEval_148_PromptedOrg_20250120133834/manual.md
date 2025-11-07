# Planet Orbit Finder

This software provides a function to determine the planets located between two given planets in the solar system, sorted by their proximity to the sun.

## Main Functionality

The main function of this software is `bf`, which takes two planet names as input and returns a tuple of planets whose orbits are located between the orbits of the two input planets. The planets are sorted by their proximity to the sun.

### Function: `bf(planet1, planet2)`

- **Input**: 
  - `planet1`: A string representing the name of the first planet.
  - `planet2`: A string representing the name of the second planet.
  
- **Output**: 
  - A tuple containing the names of the planets whose orbits are located between the orbits of `planet1` and `planet2`, sorted by proximity to the sun.
  - An empty tuple if either `planet1` or `planet2` is not a valid planet name.

- **Examples**:
  - `bf("Jupiter", "Neptune")` returns `("Saturn", "Uranus")`.
  - `bf("Earth", "Mercury")` returns `("Venus")`.
  - `bf("Mercury", "Uranus")` returns `("Venus", "Earth", "Mars", "Jupiter", "Saturn")`.

## Installation

This software does not require any external dependencies. You can run it with a standard Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are necessary as there are no external dependencies.

## Usage

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
   result = bf("Jupiter", "Neptune")
   print(result)  # Output: ("Saturn", "Uranus")
   ```

5. You can test the function with different planet names to find the planets between their orbits.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is self-contained and includes detailed docstrings explaining its usage and behavior.