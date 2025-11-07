manual.md

```
# Solar System Orbit Finder

This software provides a simple function to determine the planets located between the orbits of two given planets in our solar system. It is designed to be lightweight and efficient, requiring no external dependencies.

## Main Functionality

The core functionality of this software is encapsulated in the `bf` function. This function takes two planet names as input and returns a tuple of planet names that are located between the orbits of the two specified planets, sorted by their proximity to the sun.

### Function: `bf`

- **Input**: Two strings representing the names of planets in our solar system.
- **Output**: A tuple containing the names of planets whose orbits lie between the two specified planets. If either of the input planet names is invalid, the function returns an empty tuple.

#### Example Usage

```python
# Example 1
result = bf("Jupiter", "Neptune")
print(result)  # Output: ("Saturn", "Uranus")

# Example 2
result = bf("Earth", "Mercury")
print(result)  # Output: ("Venus")

# Example 3
result = bf("Mercury", "Uranus")
print(result)  # Output: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
```

## Installation

This software does not require any external libraries or dependencies. It is implemented purely in Python, making it easy to integrate into any Python environment.

### Quick Start

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Code**: You can directly run the Python script using a Python interpreter. Ensure you have Python installed on your machine.

```bash
python main.py
```

## Usage

To use the `bf` function, simply import it into your Python script and call it with the desired planet names. Ensure that the planet names are correctly spelled and capitalized as per the list of planets in our solar system.

```python
from main import bf

# Example usage
result = bf("Mars", "Jupiter")
print(result)  # Output: ()
```

## Notes

- The function is case-sensitive and expects the planet names to be capitalized correctly.
- The list of valid planet names includes: "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune".
- The function is designed to handle only the eight major planets of our solar system.

This software is ideal for educational purposes, astronomy enthusiasts, or anyone interested in exploring the relative positions of planets in our solar system.
```