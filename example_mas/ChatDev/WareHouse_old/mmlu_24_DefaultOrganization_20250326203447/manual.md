# Moral Scenarios Quiz User Manual

Welcome to the Moral Scenarios Quiz application! This software is designed to help users engage with moral scenarios and determine the correct moral judgment according to ordinary moral standards in the US as of 2020.

## Main Functions

The Moral Scenarios Quiz application provides the following main functions:

- **Interactive Quiz**: Users are presented with a moral scenario question and multiple-choice answers. They can select an answer and submit it to see if they are correct.
- **Feedback System**: After submitting an answer, users receive immediate feedback indicating whether their choice was correct or incorrect, along with the correct answer.

## Installation Guide

To run the Moral Scenarios Quiz application, you need to set up the environment and install the necessary dependencies. Follow the steps below:

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Clone the repository containing the application code to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your current directory to the project directory.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Use the following command to install the required dependencies listed in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

   Note: If you encounter issues with the virtual display, ensure that `Xvfb` is installed on your system. For Debian-based systems, you can install it using:

   ```bash
   sudo apt-get install xvfb
   ```

## How to Use the Application

1. **Run the Application**: Execute the main application script to start the quiz.

   ```bash
   python main.py
   ```

2. **Interact with the Quiz**: A window will appear with the moral scenarios question. Read the question and select the answer you believe is correct by clicking on the corresponding radio button.

3. **Submit Your Answer**: Click the "Submit" button to check your answer. A message box will display whether your answer is correct or incorrect, along with the correct answer.

4. **Close the Application**: Once you have completed the quiz, you can close the application window.

## Additional Information

- **Virtual Display**: The application uses a virtual display to run the GUI. Ensure that your system supports virtual displays and that `Xvfb` is installed if necessary.

- **Feedback and Support**: If you encounter any issues or have questions about the application, please contact our support team for assistance.

Enjoy exploring moral scenarios and enhancing your understanding of moral judgments with the Moral Scenarios Quiz application!