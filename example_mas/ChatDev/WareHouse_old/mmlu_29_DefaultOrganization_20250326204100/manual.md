# Moral Scenarios Quiz User Manual

Welcome to the Moral Scenarios Quiz application! This software is designed to provide an interactive experience where users can engage with moral scenarios and determine the moral correctness of actions based on ordinary moral standards in the US as of 2020.

## Main Functions

The main function of this software is to present users with moral scenarios and allow them to select the most appropriate moral judgment from a set of multiple-choice options. The application provides immediate feedback on the correctness of the user's choice.

### Features

- **Interactive Quiz Interface**: Users can read scenarios and select their answers through a user-friendly graphical interface.
- **Immediate Feedback**: After submitting an answer, users receive instant feedback on whether their choice was correct.
- **Educational Tool**: This application can be used as an educational tool to discuss and reflect on moral standards.

## Installation

To run the Moral Scenarios Quiz, you need to have Python installed on your system. Additionally, you need to install the required dependencies.

### Step-by-Step Installation Guide

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Download or clone the repository containing the application code.

3. **Install Dependencies**: Use the following command to install the required dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `pyvirtualdisplay` package, which is necessary for running the application in a headless environment.

4. **Set Up Virtual Display (Optional)**: If you are running the application in a headless environment (e.g., a server without a graphical interface), you may need to set up a virtual display using Xvfb. Install Xvfb using your package manager:

   ```bash
   sudo apt-get install xvfb
   ```

## How to Use

1. **Run the Application**: Navigate to the directory containing the `main.py` file and execute the following command to start the application:

   ```bash
   python main.py
   ```

2. **Interact with the Quiz**: The application window will open, displaying the moral scenarios and multiple-choice options. Read the scenarios carefully.

3. **Select an Answer**: Use the radio buttons to select the answer you believe is correct.

4. **Submit Your Answer**: Click the "Submit" button to check your answer. A message box will display whether your choice was correct or incorrect, along with the correct answer.

5. **Reflect and Learn**: Use the feedback provided to reflect on the moral standards and improve your understanding.

## Troubleshooting

- **No Display Found**: If you encounter an error about no display being found, ensure that you have set up a virtual display using Xvfb if running in a headless environment.

- **Dependency Issues**: If you face issues with dependencies, ensure that you have installed all required packages using the `requirements.txt` file.

## Conclusion

The Moral Scenarios Quiz is a simple yet effective tool for exploring moral judgments and standards. We hope you find it educational and engaging. For any further assistance or feedback, please contact our support team.