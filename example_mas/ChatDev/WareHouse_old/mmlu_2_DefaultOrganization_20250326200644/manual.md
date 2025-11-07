# Business Ethics Quiz Application

This user manual provides detailed instructions on how to use the Business Ethics Quiz Application, a simple graphical user interface (GUI) application designed to test your knowledge of business ethics through multiple-choice questions.

## Overview

The Business Ethics Quiz Application is a Python-based software that presents users with a multiple-choice question about business ethics. Users can select an answer and submit their choice to see if they are correct. The application provides immediate feedback on the selected answer.

## Main Features

- **Interactive GUI**: The application uses a graphical user interface to display questions and options, making it user-friendly and easy to navigate.
- **Immediate Feedback**: After submitting an answer, users receive instant feedback indicating whether their choice was correct or incorrect.
- **Educational Content**: The application is designed to enhance understanding of business ethics by providing thought-provoking questions.

## Installation

### Prerequisites

- **Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Tkinter**: This is a standard Python interface to the Tk GUI toolkit and is usually included with Python installations.

### Environment Setup

1. **Clone the Repository**: Download or clone the repository containing the application code.

2. **Install Dependencies**: The application requires `xvfb` for running in a headless environment. You can install it using your system's package manager. For example, on Ubuntu, use:
   ```bash
   sudo apt-get install xvfb
   ```

3. **Python Dependencies**: Ensure that all Python dependencies are satisfied. The application primarily uses Tkinter, which is included with Python.

### Running the Application

1. **Navigate to the Application Directory**: Open a terminal and navigate to the directory where the application files are located.

2. **Run the Application**: Execute the following command to start the application:
   ```bash
   python main.py
   ```

3. **Using the Application**: Once the application window opens:
   - Read the question displayed at the top.
   - Select one of the multiple-choice options by clicking the corresponding radio button.
   - Click the "Submit" button to check your answer.
   - A message box will display whether your answer was correct or incorrect.

## Troubleshooting

- **No Display Error**: If you encounter issues related to display, ensure that `xvfb` is properly installed and configured, especially if running in a headless environment.
- **Python Errors**: Ensure that Python is correctly installed and that you are using a compatible version.

## Conclusion

The Business Ethics Quiz Application is a simple yet effective tool for testing and improving your knowledge of business ethics. By following this manual, you should be able to install, run, and use the application with ease. Enjoy learning and testing your knowledge!