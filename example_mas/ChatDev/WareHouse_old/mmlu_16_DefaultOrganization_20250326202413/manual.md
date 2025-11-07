# Clinical Knowledge Quiz User Manual

Welcome to the Clinical Knowledge Quiz application! This software is designed to test your knowledge on clinical topics through a multiple-choice quiz format. Below is a detailed guide on how to install, set up, and use the application.

## Main Functions

The Clinical Knowledge Quiz application provides the following main functions:

- **Interactive Quiz Interface**: A graphical user interface (GUI) that presents a multiple-choice question about clinical knowledge.
- **Answer Evaluation**: The application checks the user's selected answer and provides immediate feedback on whether the answer is correct or incorrect.
- **Educational Tool**: Aimed at enhancing understanding of clinical concepts through interactive learning.

## Installation

### Prerequisites

Before installing the application, ensure that you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Download the application code from the repository or copy the provided code into a local directory.

2. **Install Dependencies**: The application requires the `pyvirtualdisplay` package. You can install it using pip:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can manually install the package:

   ```bash
   pip install pyvirtualdisplay==2.2
   ```

3. **Install Xvfb (if necessary)**: If you are running the application on a system without a display (e.g., a server), you may need to install Xvfb for a virtual display:

   ```bash
   sudo apt-get install xvfb
   ```

## How to Use

1. **Run the Application**: Navigate to the directory containing the `main.py` file and execute the script:

   ```bash
   python main.py
   ```

2. **Interact with the Quiz**: A window titled "Clinical Knowledge Quiz" will appear. Read the question and select the answer you believe is correct by clicking the corresponding radio button.

3. **Submit Your Answer**: Click the "Submit" button to check your answer. A message box will display whether your answer is correct or incorrect, along with the correct answer.

4. **Close the Application**: Once you have completed the quiz, you can close the application window.

## Troubleshooting

- **No Display Found**: If you encounter a "No display found" error, ensure that Xvfb is installed and properly configured on your system.

- **Dependencies Not Installed**: If you receive errors related to missing packages, double-check that all dependencies listed in `requirements.txt` are installed.

## Additional Information

For further assistance or to report issues, please contact the support team or visit our documentation page for more detailed guides and troubleshooting tips.

Thank you for using the Clinical Knowledge Quiz application! We hope it enhances your learning experience in clinical knowledge.