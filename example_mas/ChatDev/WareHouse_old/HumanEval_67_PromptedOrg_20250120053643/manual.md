# Fruit Distribution Software Manual

## Introduction

The Fruit Distribution software is a simple Python application designed to calculate the number of mangoes in a basket of fruits. The basket contains apples, oranges, and mangoes. Given a string that specifies the number of apples and oranges, and an integer representing the total number of fruits in the basket, the software computes the number of mangoes.

## Main Functionality

The core functionality of the software is provided by the `fruit_distribution` function. This function takes two inputs:
- A string (`s`) that describes the number of apples and oranges in the format: "X apples and Y oranges".
- An integer (`n`) that represents the total number of fruits in the basket.

The function returns an integer representing the number of mangoes in the basket.

### Example Usage

```python
# Example usage of the fruit_distribution function
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

## Installation

### Environment Setup

This project does not require any external dependencies, making it straightforward to set up. You only need to have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can run the `main.py` file directly to test the function:
   ```bash
   python main.py
   ```

## How to Use

To use the `fruit_distribution` function, you can either import it into your own Python script or run it directly from the `main.py` file. Here’s how you can use it in a script:

```python
from main import fruit_distribution

# Calculate the number of mangoes
mangoes = fruit_distribution("5 apples and 6 oranges", 19)
print(f"The number of mangoes is: {mangoes}")
```

## Conclusion

The Fruit Distribution software is a simple yet effective tool for calculating the number of mangoes in a basket of fruits. With no external dependencies required, it is easy to set up and use. This manual provides all the necessary information to get started with the software. Enjoy using the Fruit Distribution software!