# Physics Uncertainty Calculator User Manual

Welcome to the Physics Uncertainty Calculator! This software is designed to help users calculate the uncertainty in kinetic energy based on the uncertainty in speed. This manual will guide you through the installation, setup, and usage of the software.

## Introduction

The Physics Uncertainty Calculator is a simple tool that allows users to input the percentage uncertainty in speed and receive the corresponding percentage uncertainty in kinetic energy. This is particularly useful for physics students and educators who need to perform quick calculations related to experimental uncertainties.

## Main Functions

- **Calculate Kinetic Energy Uncertainty:** The software calculates the uncertainty in kinetic energy based on the inputted uncertainty in speed. Since kinetic energy is proportional to the square of speed, the uncertainty in kinetic energy is twice the uncertainty in speed.

## Installation

To use the Physics Uncertainty Calculator, you need to have Python installed on your system. Additionally, you need to install the required dependencies.

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Dependencies

The software requires the `tkinter` library for the graphical user interface. This library is included with most Python installations. However, if you encounter any issues, you can install it using the following command:

```bash
sudo apt-get install python3-tk
```

### Step 3: Download the Software

Clone the repository or download the source code files (`main.py` and `physics_calculator.py`) to your local machine.

### Step 4: Run the Software

Navigate to the directory containing the downloaded files and run the following command to start the application:

```bash
python main.py
```

## Usage

1. **Launch the Application:** Run `main.py` to open the Physics Uncertainty Calculator GUI.

2. **Enter Speed Uncertainty:** In the input field, enter the percentage uncertainty of the speed. Ensure that the value is a positive number.

3. **Calculate:** Click the "Calculate" button. The software will compute the kinetic energy uncertainty and display the result.

4. **View Result:** The calculated kinetic energy uncertainty will be displayed below the input field.

## Troubleshooting

- **Invalid Input:** If you enter a negative value or a non-numeric input, an error message will be displayed. Please enter a valid positive number.

- **Display Issues:** If you encounter issues with the graphical display, ensure that your environment supports `tkinter`.

## Conclusion

The Physics Uncertainty Calculator is a straightforward tool for calculating uncertainties in physics experiments. By following this manual, you should be able to install, set up, and use the software effectively. If you have any further questions or require support, please contact our support team.

Thank you for using the Physics Uncertainty Calculator!