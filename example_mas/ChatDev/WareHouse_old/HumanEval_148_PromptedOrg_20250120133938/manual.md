# Planet Orbit Finder

This software provides a function to determine the planets located between the orbits of two specified planets in our solar system, based on their proximity to the Sun.

## Main Functionality

The primary function of this software is `bf(planet1, planet2)`, which takes two planet names as input and returns a tuple of planet names that are located between the orbits of the specified planets. The planets are sorted by their proximity to the Sun. If either of the input planet names is incorrect, the function returns an empty tuple.

### Example Usage

- `bf("Jupiter", "Neptune")` returns `("Saturn", "Uranus")`
- `bf("Earth", "Mercury")` returns `("Venus")`
- `bf("Mercury", "Uranus")` returns `("Venus", "Earth", "Mars", "Jupiter", "Saturn")`

## Installation

This project does not require any external dependencies, so there is no need to install additional packages. You can simply download the `main.py` file and run it using Python.

### Quick Start

1. **Download the Code:**
   - Obtain the `main.py` file from the repository.

2. **Run the Code:**
   - Ensure you have Python installed on your system.
   - Execute the `main.py` file using a Python interpreter.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function:**
   - Import the `bf` function from the `main.py` file into your Python script or interactive session.

   ```python
   from main import bf
   ```

2. **Call the Function:**
   - Use the `bf` function with the names of two planets as arguments to find the planets between their orbits.

   ```python
   result = bf("Mars", "Neptune")
   print(result)  # Output: ('Jupiter', 'Saturn', 'Uranus')
   ```

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is documented with examples to help you understand its usage and expected outputs.

## Support

If you encounter any issues or have questions about using this software, please contact our support team for assistance. We are here to help you make the most of this tool.