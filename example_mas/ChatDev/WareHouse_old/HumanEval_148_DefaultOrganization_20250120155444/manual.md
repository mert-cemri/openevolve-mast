manual.md

```
# Solar System Orbit Finder

This software provides a function to determine the planets located between the orbits of two given planets in the solar system. It is a simple Python application that can be used to understand the relative positions of planets based on their proximity to the Sun.

## Main Functionality

The main function of this software is `bf(planet1, planet2)`, which takes two planet names as input and returns a tuple of planet names that are located between the orbits of the two specified planets. The planets are sorted by their proximity to the Sun.

### Function Details

- **Function Name:** `bf`
- **Parameters:**
  - `planet1` (str): The name of the first planet.
  - `planet2` (str): The name of the second planet.
- **Returns:** A tuple containing the names of planets between `planet1` and `planet2`. If either planet name is invalid, it returns an empty tuple.

### Examples

- `bf("Jupiter", "Neptune")` returns `("Saturn", "Uranus")`
- `bf("Earth", "Mercury")` returns `("Venus")`
- `bf("Mercury", "Uranus")` returns `("Venus", "Earth", "Mars", "Jupiter", "Saturn")`

## Installation

To use this software, you need to have Python installed on your system. The software does not have any external dependencies, so you do not need to install any additional packages.

### Steps to Install Python

1. **Download Python:**
   - Visit the official Python website at [python.org](https://www.python.org/).
   - Download the latest version of Python for your operating system.

2. **Install Python:**
   - Follow the installation instructions provided on the Python website for your specific operating system.

3. **Verify Installation:**
   - Open a terminal or command prompt.
   - Type `python --version` to verify that Python is installed correctly.

## How to Use

1. **Clone the Repository:**
   - Clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.

3. **Run the Function:**
   - Open a Python interactive shell by typing `python` in the terminal.
   - Import the function by typing `from main import bf`.
   - Call the function with desired planet names, e.g., `bf("Earth", "Mars")`.

## Documentation

For further details and documentation, please refer to the comments within the `main.py` file. The function is well-documented with examples to help you understand its usage.

```