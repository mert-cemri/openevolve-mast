# Math Quiz Application User Manual

Welcome to the Math Quiz Application! This software is designed to provide a simple and interactive way to solve elementary mathematics questions using a graphical user interface (GUI). Below, you'll find detailed instructions on how to install, set up, and use the application.

## Main Functions

The Math Quiz Application offers the following main functions:

- **Display a Math Question**: The application presents a math question related to elementary mathematics.
- **Provide Multiple Choice Options**: Users are given multiple choice options to select the correct answer.
- **Calculate and Display the Answer**: Upon user request, the application calculates the correct answer and displays it.

## Quick Install

To get started with the Math Quiz Application, you need to have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

### Step-by-Step Installation

1. **Clone the Repository**: First, clone the repository containing the Math Quiz Application code to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your current directory to the project directory.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: The application requires the `tkinter` library, which is included with Python by default. Ensure your Python installation includes `tkinter`.

4. **Run the Application**: Execute the main application script to start the Math Quiz Application.

   ```bash
   python main.py
   ```

## How to Use the Application

1. **Launch the Application**: Run the `main.py` script to open the Math Quiz Application window.

2. **Read the Question**: The application will display a math question related to elementary mathematics.

3. **View the Options**: Below the question, you will see multiple choice options labeled with indices (0, 1, 2, 3).

4. **Calculate the Answer**: Click the "Calculate Answer" button to compute the correct answer based on the provided question.

5. **View the Result**: A message box will display the correct answer in the format "The answer is (X)", where X is the index of the correct option.

## Troubleshooting

- **No Display Found**: If you encounter an error stating "No display found. Running in headless mode," ensure you are running the application in an environment with a graphical display.

- **Error Message**: If the application cannot determine the correct answer, an error message will be displayed. Ensure the logic in the `calculate_answer` function is correct.

## Additional Information

For further assistance or to report issues, please contact the support team or refer to the project's repository for updates and additional documentation.

Enjoy using the Math Quiz Application to enhance your elementary mathematics skills!