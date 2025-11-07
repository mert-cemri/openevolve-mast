# High School Government and Politics Quiz Application

This application is a simple graphical user interface (GUI) quiz designed to test knowledge on high school government and politics topics. It is built using Python's Tkinter library.

## Main Functions

- **Question Display**: The application presents a multiple-choice question about government and politics.
- **Answer Selection**: Users can select one of the four provided answer options.
- **Answer Submission**: Users submit their selected answer to see if it is correct.
- **Feedback**: The application provides immediate feedback on whether the selected answer is correct or incorrect.

## Installation

### Prerequisites

- **Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/).
- **Tkinter**: Tkinter is included with standard Python installations. No additional installation is required for Tkinter.

### Environment Setup

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Move into the project directory.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Although there are no external dependencies required for this project, ensure your Python environment is set up correctly.

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file is included for completeness but does not list any external packages since none are required.

## Usage

1. **Run the Application**: Execute the main application file to start the quiz.

   ```bash
   python main.py
   ```

2. **Interact with the GUI**:
   - Read the question displayed at the top of the window.
   - Select your answer by clicking on one of the radio buttons corresponding to the answer choices.
   - Click the "Submit" button to check your answer.

3. **Receive Feedback**: A message box will appear indicating whether your answer was correct or incorrect. The correct answer is also displayed.

## Additional Information

- **Headless Environments**: If running the application in a headless environment (e.g., a server without a display), ensure that the `DISPLAY` environment variable is set appropriately. The application attempts to set a default display if none is detected.

- **Customization**: The application can be customized to include more questions or different topics by modifying the `create_widgets` method in the `MainApp` class.

This application serves as an educational tool for students and educators interested in government and politics. Enjoy testing your knowledge!