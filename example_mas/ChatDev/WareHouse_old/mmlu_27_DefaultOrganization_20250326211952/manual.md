# Professional Law Quiz Application

Welcome to the Professional Law Quiz Application! This software is designed to provide users with an interactive experience to test their knowledge on professional law through multiple-choice questions.

## Main Functions

The application offers the following main functions:

- **Interactive Quiz Interface**: Users can engage with a graphical user interface (GUI) to answer multiple-choice questions related to professional law.
- **Immediate Feedback**: After submitting an answer, users receive immediate feedback on whether their answer was correct or incorrect.
- **Educational Content**: The questions are designed to educate users on important legal principles and scenarios.

## Installation Guide

### System Requirements

- A system with a graphical interface (GUI support).
- Python 3.x installed on your system.

### Environment Setup

1. **Clone the Repository**: Start by cloning the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Ensure you have the necessary Python packages installed. You can use `pip` to install `tkinter` if it's not already available on your system.
   ```bash
   pip install tk
   ```

3. **Check Display Environment**: Make sure your system supports GUI applications. If you are running on a headless server, you might need to set up a virtual display.

## How to Use the Application

1. **Run the Application**: Navigate to the directory where the application files are located and run the `main.py` file.
   ```bash
   python main.py
   ```

2. **Answer the Question**: Once the application is running, read the question displayed on the GUI and select the answer you believe is correct by clicking on the corresponding radio button.

3. **Submit Your Answer**: Click the "Submit" button to check your answer. A message box will appear indicating whether your answer was correct or incorrect.

4. **Review Feedback**: Use the feedback provided to understand the correct answer and learn more about the legal principles involved.

## Additional Information

- **Customization**: You can add more questions by modifying the `question.py` file and updating the `MainApp` class in `main.py` to include new instances of the `Question` class.
- **Support**: For any issues or questions, please contact our support team or refer to the documentation provided in the repository.

Enjoy testing your knowledge with the Professional Law Quiz Application!