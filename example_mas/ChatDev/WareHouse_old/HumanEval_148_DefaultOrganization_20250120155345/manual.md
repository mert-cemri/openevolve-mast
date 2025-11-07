# Planetary Orbit Finder

This software provides a function to determine the planets located between two given planets in our solar system. It is designed to help users identify the sequence of planets based on their proximity to the sun.

## Main Functionality

The core functionality of this software is provided by the `bf` function, which takes two planet names as input and returns a tuple of planets whose orbits are located between the orbits of the two specified planets.

### Function: `bf(planet1, planet2)`

- **Parameters**:
  - `planet1`: A string representing the name of the first planet.
  - `planet2`: A string representing the name of the second planet.

- **Returns**:
  - A tuple containing the names of planets located between `planet1` and `planet2`, sorted by their proximity to the sun.
  - An empty tuple if either `planet1` or `planet2` is not a valid planet name.

- **Examples**:
  - `bf("Jupiter", "Neptune")` returns `("Saturn", "Uranus")`
  - `bf("Earth", "Mercury")` returns `("Venus")`
  - `bf("Mercury", "Uranus")` returns `("Venus", "Earth", "Mars", "Jupiter", "Saturn")`

## Installation

This software is implemented in Python and does not require any external dependencies beyond the standard Python library. To use the software, ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

3. **Run the Code**: You can execute the function by importing it into your Python script or interactive shell.

## Usage

To use the `bf` function, follow these steps:

1. **Import the Function**: Ensure that the `main.py` file is in your working directory or your Python path.

2. **Call the Function**: Use the function by passing the names of two planets as arguments.

```python
from main import bf

# Example usage
result = bf("Jupiter", "Neptune")
print(result)  # Output: ("Saturn", "Uranus")
```

## Documentation

For further details on the usage and examples, please refer to the comments within the `main.py` file. The function is straightforward and designed to be user-friendly for those familiar with basic Python programming.

This manual provides all necessary information to install and use the software effectively. If you encounter any issues or have questions, please refer to the comments in the code or contact our support team for assistance.