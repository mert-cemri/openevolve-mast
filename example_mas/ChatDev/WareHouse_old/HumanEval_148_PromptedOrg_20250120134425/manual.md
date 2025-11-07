# Planet Orbit Finder

This software provides a function to determine the planets located between the orbits of two given planets in our solar system. It is a simple Python application that does not require any external dependencies.

## Main Functionality

The main function of this software is `bf(planet1, planet2)`, which takes the names of two planets as input and returns a tuple of planet names whose orbits are located between the orbits of the two given planets. The planets are sorted by their proximity to the sun. If either of the input planet names is incorrect, the function returns an empty tuple.

### Examples

- `bf("Jupiter", "Neptune")` returns `("Saturn", "Uranus")`
- `bf("Earth", "Mercury")` returns `("Venus")`
- `bf("Mercury", "Uranus")` returns `("Venus", "Earth", "Mars", "Jupiter", "Saturn")`

## Installation

Since this project does not require any external dependencies, you can run it directly with Python. Ensure you have Python installed on your system.

### Steps to Install

1. **Clone the Repository:**
   - Use `git clone <repository-url>` to clone the repository to your local machine.

2. **Navigate to the Project Directory:**
   - Use `cd <project-directory>` to navigate to the directory where the project is located.

3. **Run the Code:**
   - You can run the code directly using Python. Open a terminal and execute the following command:
     ```bash
     python main.py
     ```

## How to Use

1. **Import the Function:**
   - In your Python script or interactive shell, import the function using:
     ```python
     from main import bf
     ```

2. **Call the Function:**
   - Use the function by passing the names of two planets as strings:
     ```python
     result = bf("Mars", "Jupiter")
     print(result)  # Output: ()
     ```

3. **Handle the Output:**
   - The function will return a tuple of planet names. If the input is invalid, it will return an empty tuple.

## Documentation

For further details on how the function works, please refer to the docstring provided in the `main.py` file. The docstring includes a description of the function, its parameters, and examples of its usage.

This software is designed to be simple and straightforward, making it easy for users to integrate the function into their own projects or use it for educational purposes.