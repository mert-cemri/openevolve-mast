manual.md

```
# Planet Orbit Finder

This software provides a function to determine the planets located between the orbits of two given planets in our solar system. It is a simple utility that can be used for educational purposes or as a component in larger astronomical applications.

## Main Functionality

The main function provided by this software is `bf(planet1, planet2)`. This function takes two planet names as input and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by their proximity to the sun. If either of the planet names is incorrect, the function returns an empty tuple.

### Examples

- `bf("Jupiter", "Neptune")` returns `("Saturn", "Uranus")`
- `bf("Earth", "Mercury")` returns `("Venus")`
- `bf("Mercury", "Uranus")` returns `("Venus", "Earth", "Mars", "Jupiter", "Saturn")`

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are required since there are no external dependencies.

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

5. You can test the function with different planet names to see the planets located between their orbits.

## Documentation

This software is designed to be simple and easy to use. For any further questions or support, please contact our support team or refer to the comments within the code for additional guidance.

```