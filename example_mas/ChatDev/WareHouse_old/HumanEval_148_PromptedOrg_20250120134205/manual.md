# Planetary Orbit Finder

This software provides a function to determine the planets located between two given planets in the solar system, based on their proximity to the Sun.

## Main Functionality

The main function provided by this software is `bf(planet1, planet2)`. This function takes two planet names as input and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by their proximity to the Sun. If either of the planet names is incorrect, the function returns an empty tuple.

### Example Usage

- `bf("Jupiter", "Neptune")` returns `("Saturn", "Uranus")`
- `bf("Earth", "Mercury")` returns `("Venus")`
- `bf("Mercury", "Uranus")` returns `("Venus", "Earth", "Mars", "Jupiter", "Saturn")`

## Installation

This software does not require any external dependencies, so you can use it directly in your Python environment. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. **Run the Code**: You can use the function directly in a Python script or interactive session. Here's how you can use it in a Python script:

   ```python
   from main import bf

   # Example usage
   result = bf("Jupiter", "Neptune")
   print(result)  # Output: ("Saturn", "Uranus")
   ```

4. **Interactive Python Session**: Alternatively, you can use the function in an interactive Python session:

   ```bash
   python
   ```

   Then, within the Python shell:

   ```python
   from main import bf

   # Example usage
   result = bf("Mercury", "Uranus")
   print(result)  # Output: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
   ```

## Documentation

The function is straightforward and does not require additional configuration. Ensure that the planet names provided are correctly spelled and are among the eight recognized planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.

For any further questions or support, please contact our support team.