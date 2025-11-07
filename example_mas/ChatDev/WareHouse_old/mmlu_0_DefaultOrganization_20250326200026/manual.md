# Accounting Question Application

This application is designed to help users understand the impact of changing inventory valuation methods from FIFO to LIFO during periods of inflation. It provides a graphical user interface (GUI) for users to answer a multiple-choice question related to professional accounting.

## Main Functions

- **Question Display**: The application displays a question about the effects of switching from FIFO to LIFO on ending inventory and income tax payable during inflation.
- **Answer Selection**: Users can select one of the multiple-choice answers provided.
- **Answer Validation**: The application checks the selected answer against the correct answer and provides feedback to the user.

## Installation

### Environment Dependencies

To run this application, you need to have Python installed on your system. Additionally, the application uses the `tkinter` library for the GUI, which is included with standard Python installations.

### Quick Install

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Verify Tkinter**: `tkinter` is included with Python, but you can verify its installation by running the following command in your terminal or command prompt:
   ```bash
   python -m tkinter
   ```
   If a small window appears, `tkinter` is installed correctly.

## How to Use the Application

1. **Run the Application**: Open a terminal or command prompt and navigate to the directory containing `main.py`. Run the application using the following command:
   ```bash
   python main.py
   ```

2. **Interact with the GUI**:
   - Read the question displayed in the application window.
   - Select one of the answer options by clicking the corresponding radio button.
   - Click the "Submit" button to check your answer.

3. **Receive Feedback**: A message box will appear indicating whether your answer is correct or incorrect. If incorrect, the correct answer will be displayed.

## Notes

- Ensure you are running the application in an environment with a graphical display, as it requires a GUI to function.
- The correct answer to the question is option 0: "Lower Lower", as during inflation, LIFO results in lower ending inventory and lower income tax payable compared to FIFO.

This application is a simple educational tool for understanding the effects of inventory valuation methods during inflationary periods. Enjoy learning!