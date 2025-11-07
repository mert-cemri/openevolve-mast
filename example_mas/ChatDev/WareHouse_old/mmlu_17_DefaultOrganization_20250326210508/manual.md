# Clinical Knowledge Quiz User Manual

Welcome to the Clinical Knowledge Quiz application! This software is designed to help users test their knowledge on clinical topics through a multiple-choice question interface. Below is a detailed guide on how to install, set up, and use the application.

## Main Functions

The Clinical Knowledge Quiz application provides the following main functions:

- **Interactive Quiz Interface**: Users can engage with multiple-choice questions through a graphical user interface (GUI) built with Tkinter.
- **Immediate Feedback**: After selecting an answer, users receive instant feedback on whether their choice was correct or incorrect.
- **Educational Tool**: Designed to enhance learning and retention of clinical knowledge through active participation.

## Installation

### Prerequisites

Before installing the application, ensure you have the following:

- **Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Tkinter**: This is a standard GUI toolkit for Python. It is usually included with Python installations, but if not, you can install it via your package manager.
- **Optional**: If you plan to run the application in a headless environment (e.g., a server without a display), you will need `pyvirtualdisplay`.

### Quick Install

1. **Clone the Repository**: Download the code from the repository or copy the provided code files (`main.py` and `question.py`) into a directory on your system.

2. **Install Dependencies**: 
   - If you are running the application in a headless environment, install `pyvirtualdisplay` using pip:
     ```bash
     pip install pyvirtualdisplay
     ```

## How to Use

### Running the Application

1. **Start the Application**: Navigate to the directory containing `main.py` and run the following command in your terminal or command prompt:
   ```bash
   python main.py
   ```

2. **Interacting with the Quiz**:
   - A window titled "Clinical Knowledge Quiz" will appear.
   - Read the question displayed at the top of the window.
   - Select your answer by clicking on one of the radio buttons corresponding to the options provided.
   - Click the "Submit" button to check your answer.

3. **Receiving Feedback**:
   - A message box will appear indicating whether your answer was correct or incorrect.
   - The correct answer will be displayed in the message box for your reference.

### Headless Environment

If you are running the application on a server or a system without a display, ensure `pyvirtualdisplay` is installed and configured as described in the installation section. The application will attempt to use a virtual display to render the GUI.

## Conclusion

The Clinical Knowledge Quiz application is a simple yet effective tool for testing and improving your clinical knowledge. By following the instructions in this manual, you should be able to set up and use the application with ease. Enjoy learning and testing your knowledge!