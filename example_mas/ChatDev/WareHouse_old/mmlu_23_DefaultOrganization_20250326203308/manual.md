# Business Ethics Quiz Application

This user manual provides detailed instructions on how to install, set up, and use the Business Ethics Quiz Application. This application is designed to help users test their knowledge of business ethics through a multiple-choice quiz format.

## Main Functions

The Business Ethics Quiz Application is a simple graphical user interface (GUI) application that allows users to:

- **View a Business Ethics Question**: The application presents a multiple-choice question related to business ethics.
- **Select an Answer**: Users can select one of the provided answer options using radio buttons.
- **Submit an Answer**: Users can submit their selected answer to check if it is correct.
- **Receive Feedback**: The application provides immediate feedback on whether the selected answer is correct or incorrect.

## Installation

### Prerequisites

Before installing the application, ensure that you have the following installed on your system:

- **Python**: The application is written in Python, so you need Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Tkinter**: This is a standard GUI toolkit for Python. It is usually included with Python installations, but you may need to install it separately depending on your operating system.
- **Virtual Display (Optional)**: If you are running the application in a headless environment (e.g., a server without a display), you will need `pyvirtualdisplay` and `Xvfb`.

### Installing Dependencies

To install the necessary Python packages, you can use `pip`. Open your terminal or command prompt and run the following command:

```bash
pip install pyvirtualdisplay
```

Note: `pyvirtualdisplay` is only required if you are running the application in a headless environment.

## Usage

### Running the Application

1. **Clone the Repository**: First, clone the repository containing the application code to your local machine.

2. **Navigate to the Application Directory**: Open your terminal or command prompt and navigate to the directory where the application code is located.

3. **Run the Application**: Execute the following command to start the application:

   ```bash
   python main.py
   ```

   If you are running in a headless environment, ensure that `pyvirtualdisplay` and `Xvfb` are installed and configured correctly.

### Using the Application

1. **View the Question**: Once the application starts, you will see a window displaying a business ethics question.

2. **Select an Answer**: Use the radio buttons to select the answer you believe is correct.

3. **Submit Your Answer**: Click the "Submit" button to check your answer.

4. **Receive Feedback**: A message box will appear indicating whether your answer is correct or incorrect. If incorrect, you can try again.

## Troubleshooting

- **No GUI Display**: If the application does not display a GUI, ensure that Tkinter is installed correctly. If running in a headless environment, check the configuration of `pyvirtualdisplay` and `Xvfb`.
- **Dependencies Not Installed**: Ensure all required Python packages are installed using `pip`.

For further assistance, please contact our support team. We hope you enjoy using the Business Ethics Quiz Application to enhance your understanding of business ethics!