# Legal Question Evaluator User Manual

Welcome to the Legal Question Evaluator, a software application designed to assist users in evaluating legal questions related to property law. This user manual will guide you through the installation, main functions, and usage of the software.

## Main Functions

The Legal Question Evaluator is a tool that allows users to input legal questions and receive an evaluation based on predefined logic. The software is particularly focused on questions related to property law, such as issues involving deeds, titles, and mortgages. The main functions include:

- **Input Legal Questions**: Users can enter legal questions into the application.
- **Evaluate Questions**: The application evaluates the question using a set of predefined rules and logic.
- **Display Answers**: The application provides the most likely answer to the question based on the evaluation.

## Installation

### System Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

### Installation Steps

1. **Clone the Repository**: Download or clone the repository containing the Legal Question Evaluator code to your local machine.

2. **Set Up Python Environment**: Ensure you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

3. **Install Dependencies**: The application does not require any external dependencies beyond Python and Tkinter. However, ensure that Tkinter is installed and functioning correctly on your system.

4. **Run the Application**: Navigate to the directory containing the `main.py` file and execute the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

   This will start the application and open the graphical user interface (GUI).

## How to Use

1. **Open the Application**: After running `main.py`, a GUI window will appear.

2. **Enter Your Question**: In the text area provided, type your legal question. Ensure that the question is clear and relevant to property law topics.

3. **Evaluate the Question**: Click the "Evaluate" button to process your question. The application will analyze the question and determine the most appropriate answer based on its logic.

4. **View the Answer**: A message box will display the answer in the format "The answer is (X)", where X is the index of the answer (0, 1, 2, or 3).

5. **Error Handling**: If the application cannot determine an answer, it will display an error message. Ensure your question is correctly formatted and relevant to the application's focus area.

## Troubleshooting

- **Tkinter Errors**: If you encounter issues with Tkinter, ensure that it is correctly installed and configured on your system. Refer to the [Tkinter documentation](https://docs.python.org/3/library/tkinter.html) for assistance.

- **Graphical Display Issues**: The application requires a graphical display to function. If running on a server or environment without a GUI, consider using a local machine with a display.

## Conclusion

The Legal Question Evaluator is a simple yet powerful tool for evaluating legal questions related to property law. By following this manual, you should be able to install, run, and effectively use the application to obtain answers to your legal queries. If you have any further questions or require support, please reach out to our development team.