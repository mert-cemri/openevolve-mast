# Law Quiz App User Manual

Welcome to the Law Quiz App, a simple yet powerful tool designed to help users evaluate legal questions based on predefined legal principles. This user manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use the application effectively.

## Main Functions

The Law Quiz App is designed to:

- **Evaluate Legal Questions**: Users can input legal questions related to specific scenarios, and the app will provide the correct answer based on predefined legal principles.
- **Graphical User Interface (GUI)**: The app features a user-friendly GUI that allows users to easily input questions and receive answers.

## Installation

### Prerequisites

- **Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Download the project files to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Open a terminal and navigate to the directory where the project files are located.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: The project does not require any external dependencies, so you can skip this step.

4. **Run the Application**: Execute the main application file to start the GUI.

   ```bash
   python main.py
   ```

## How to Use the Law Quiz App

1. **Launch the Application**: After running `main.py`, the GUI window will open.

2. **Enter a Legal Question**: Type your legal question into the input field. Ensure that the question matches the predefined format for accurate evaluation.

3. **Submit the Question**: Click the "Submit" button to evaluate the question.

4. **View the Answer**: The answer will be displayed below the input field in the format "The answer is (X)", where X is the index of the correct answer.

## Example Usage

- **Question**: "While a ski lift was ascending the mountain, the overhead cable broke, dropping a skier 15 feet to the ground. The skier suffered a broken pelvis on account of the fall. Thereafter, the skier sued the ski resort alleging negligent maintenance of the ski lift machinery. The ski resort's skier's attorney took a discovery deposition of a witness who was seated behind the skier at the time of the accident. The witness died shortly after the deposition. At trial, the skier offers the witness's deposition testimony into evidence. Upon objection by the ski resort's attorney, the deposition is"

- **Expected Answer**: "The answer is (0)"

## Troubleshooting

- **Question Not Recognized**: Ensure that the question is entered exactly as defined in the application. The app currently supports a specific predefined question format.

- **GUI Not Displaying**: If running in a headless environment (e.g., a server without a display), the GUI will not be displayed. Ensure you are running the application on a system with a graphical interface.

## Support

For further assistance, please contact our support team at support@chatdev.com.

Thank you for using the Law Quiz App! We hope it enhances your understanding of legal principles.