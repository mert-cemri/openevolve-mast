# Professional Law Quiz User Manual

Welcome to the Professional Law Quiz application, a tool designed to help users test their knowledge of professional law through multiple-choice questions. This manual will guide you through the installation process, main functions, and usage of the software.

## Main Functions

The Professional Law Quiz application is a graphical user interface (GUI) that allows users to:

- **Display a Law Question**: The application presents a multiple-choice question related to professional law.
- **Select an Answer**: Users can choose from four possible answers using radio buttons.
- **Submit an Answer**: After selecting an answer, users can submit their choice to see if it is correct.
- **Receive Feedback**: The application provides immediate feedback, indicating whether the selected answer is correct or incorrect.

## Installation

To run the Professional Law Quiz application, you need to have Python installed on your system. Additionally, you will need to install the Tkinter library, which is included with most Python installations. Follow these steps to set up the environment:

1. **Install Python**: If you do not have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/).

2. **Verify Tkinter Installation**: Tkinter is included with standard Python installations. You can verify its presence by running the following command in your terminal or command prompt:
   ```bash
   python -m tkinter
   ```
   If a small window appears, Tkinter is installed correctly.

3. **Install Additional Dependencies**: The application uses Xvfb for virtual display management. Install it using your package manager. For example, on Ubuntu, you can run:
   ```bash
   sudo apt-get install xvfb
   ```

## How to Use the Application

1. **Run the Application**: Navigate to the directory containing the `main.py` file and execute the following command in your terminal or command prompt:
   ```bash
   python main.py
   ```

2. **Interact with the GUI**: Once the application starts, a window titled "Professional Law Quiz" will appear.

3. **Read the Question**: The main window displays a professional law question. Read it carefully.

4. **Select an Answer**: Use the radio buttons to select one of the four provided answers.

5. **Submit Your Answer**: Click the "Submit" button to check if your selected answer is correct.

6. **View Feedback**: A message box will appear, indicating whether your answer is correct or incorrect. The correct answer is also displayed for your reference.

7. **Close the Application**: You can close the application window when you are done.

## Troubleshooting

- **Tkinter Not Found**: If you encounter issues with Tkinter, ensure that your Python installation includes Tkinter. Reinstall Python if necessary.

- **Xvfb Issues**: If the application does not start due to display issues, ensure that Xvfb is installed and running correctly.

We hope you find the Professional Law Quiz application useful for enhancing your knowledge of professional law. If you have any questions or need further assistance, please feel free to reach out to our support team.