# Legal Question Answering Application

This user manual provides detailed instructions on how to use the Legal Question Answering Application, which is designed to assist users in determining the correct answers to legal multiple-choice questions based on legal principles.

## Main Functions

The Legal Question Answering Application offers the following main functions:

- **Question Input**: Users can input legal questions into the application.
- **Options Input**: Users can enter multiple-choice options for the question.
- **Answer Determination**: The application uses legal reasoning to determine the correct answer based on the input question and options.
- **Answer Display**: The application displays the determined answer in the format "The answer is (X)", where X is the index of the correct option.

## Installation

### Environment Dependencies

To run the Legal Question Answering Application, you need to have the following dependencies installed:

- Python 3.x
- Tkinter (usually included with Python)
- pyvirtualdisplay (optional, for headless environments)

### Installation Steps

1. **Clone the Repository**: Clone the repository containing the application code to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your working directory to the project directory.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Install the required Python packages. If you are running the application in a headless environment, you may need to install `pyvirtualdisplay`.

   ```bash
   pip install pyvirtualdisplay
   ```

## Usage

### Running the Application

1. **Start the Application**: Run the `main.py` script to start the application.

   ```bash
   python main.py
   ```

2. **Enter the Question**: In the application window, enter the legal question in the "Enter the question:" text area.

3. **Enter the Options**: Enter the multiple-choice options in the "Enter the options (separated by new lines):" text area. Each option should be on a new line.

4. **Submit the Question**: Click the "Submit" button to process the question and options.

5. **View the Answer**: The application will display the determined answer below the "Submit" button in the format "The answer is (X)".

### Example

For the provided legal question about the admissibility of deposition testimony, enter the question and options as described, and the application will determine that the correct answer is option 0: "admissible as former testimony".

## Additional Information

- **Headless Environments**: If you are running the application on a server or in an environment without a display, ensure that `pyvirtualdisplay` is installed to simulate a display.

- **Legal Reasoning**: The application uses predefined legal reasoning logic to determine the correct answer. This logic is based on legal principles and may need to be updated for different types of legal questions.

For further assistance or inquiries, please contact the development team at ChatDev.