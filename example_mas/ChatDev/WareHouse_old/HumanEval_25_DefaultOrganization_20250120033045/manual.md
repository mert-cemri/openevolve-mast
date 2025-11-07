# Factorize

A simple Python application to factorize integers into their prime factors.

## Overview

The `factorize` function takes an integer as input and returns a list of its prime factors, ordered from smallest to largest. Each factor is listed as many times as it appears in the factorization of the number.

### Example Usage

- `factorize(8)` returns `[2, 2, 2]`
- `factorize(25)` returns `[5, 5]`
- `factorize(70)` returns `[2, 5, 7]`

## Installation

This application does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**

   Clone the repository to your local machine using:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned directory.

3. **Run the Application:**

   Since there are no external dependencies, you can directly run the `main.py` file:

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function:**

   If you want to use the `factorize` function in your own scripts, you can import it:

   ```python
   from main import factorize
   ```

2. **Call the Function:**

   Use the function by passing an integer to it:

   ```python
   result = factorize(56)
   print(result)  # Output: [2, 2, 2, 7]
   ```

## Documentation

The `factorize` function is straightforward and does not require additional configuration or setup. It efficiently computes the prime factors of the given integer using a simple algorithm.

For any further questions or support, please contact the development team at ChatDev.