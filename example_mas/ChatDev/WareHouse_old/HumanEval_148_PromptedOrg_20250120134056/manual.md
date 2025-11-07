# Planet Orbit Finder

This software module provides a function to determine the planets located between the orbits of two given planets in our solar system. It is a simple utility that can be used to understand the relative positions of planets based on their proximity to the Sun.

## Main Functionality

The primary function of this software is `bf`, which takes two planet names as input and returns a tuple of planet names that are located between the orbits of the two specified planets. The planets are sorted by their proximity to the Sun.

### Function: `bf`

- **Input**: Two strings representing the names of planets (e.g., "Earth", "Mars").
- **Output**: A tuple containing the names of planets whose orbits are located between the orbits of the two input planets. If either of the input planet names is incorrect, the function returns an empty tuple.

### Examples

- `bf("Jupiter", "Neptune")` returns `("Saturn", "Uranus")`
- `bf("Earth", "Mercury")` returns `("Venus")`
- `bf("Mercury", "Uranus")` returns `("Venus", "Earth", "Mars", "Jupiter", "Saturn")`

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Start

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can use the function in a Python script or an interactive Python session.

```python
from main import bf

# Example usage
result = bf("Earth", "Mars")
print(result)  # Output: ()
```

## Usage

To use the `bf` function, simply import it from the `main.py` file and call it with the desired planet names. Ensure that the planet names are spelled correctly and are among the eight recognized planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.

## Documentation

For further details on how to use the function and examples, please refer to the comments within the `main.py` file. The function is straightforward and designed to be user-friendly for quick integration into other projects or for educational purposes.

This module is ideal for educational purposes, astronomy enthusiasts, or developers needing a simple utility to determine planetary positions relative to each other.