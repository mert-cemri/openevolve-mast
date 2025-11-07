manual.md

```
# Solar System Planets Function

This software provides a simple Python function to determine the planets located between two given planets in our solar system. The function is designed to be straightforward and efficient, making it easy to integrate into larger projects or use as a standalone utility.

## Main Functionality

The primary function provided by this software is `bf(planet1, planet2)`. This function takes two planet names as input and returns a tuple containing all planets whose orbits are located between the orbits of the two specified planets, sorted by their proximity to the sun. If either of the input planet names is incorrect, the function returns an empty tuple.

### Examples

- `bf("Jupiter", "Neptune")` returns `("Saturn", "Uranus")`
- `bf("Earth", "Mercury")` returns `("Venus")`
- `bf("Mercury", "Uranus")` returns `("Venus", "Earth", "Mars", "Jupiter", "Saturn")`

## Installation

This project does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Project Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can directly run the `main.py` file in a Python environment to test the function.

## Usage

To use the function, follow these steps:

1. **Open a Python Environment**: You can use any Python IDE or a simple command-line interface.

2. **Import the Function**: If you are using the function in another script, import it using:
   ```python
   from main import bf
   ```

3. **Call the Function**: Pass the names of the two planets as strings to the function:
   ```python
   result = bf("Earth", "Mars")
   print(result)  # Output will be: ()
   ```

## Documentation

For further details, refer to the comments within the `main.py` file. The function is well-documented to provide clarity on its usage and expected behavior.

## Support

For any issues or questions, please contact our support team or refer to the project's repository for updates and additional information.
```
