# Legal Question Evaluator User Manual

Welcome to the Legal Question Evaluator, a software application designed to assist users in evaluating legal questions based on the Rule in Shelley's Case. This manual provides a comprehensive guide on how to install, configure, and use the software effectively.

## Table of Contents

1. [Introduction](#introduction)
2. [Main Functions](#main-functions)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Troubleshooting](#troubleshooting)
6. [Support](#support)

## Introduction

The Legal Question Evaluator is a Python-based application that allows users to input legal questions and receive answers based on predefined legal rules. The current version focuses on questions related to the Rule in Shelley's Case, a common law doctrine affecting property conveyance.

## Main Functions

- **Evaluate Legal Questions:** Input a legal question related to the Rule in Shelley's Case and receive an answer based on the software's logic.
- **Graphical User Interface (GUI):** A user-friendly interface built with Tkinter for easy interaction.
- **Virtual Display Support:** Automatically sets up a virtual display if running in a headless environment.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- `pip` package manager for installing dependencies.

### Quick Install

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   Use the following command to install necessary Python packages:

   ```bash
   pip install tkinter pyvirtualdisplay
   ```

   Note: If you are running the application in a headless environment (e.g., a server without a graphical interface), ensure that `Xvfb` is installed:

   ```bash
   sudo apt-get install xvfb
   ```

## Usage

1. **Start the Application:**

   Navigate to the directory containing `main.py` and run the following command:

   ```bash
   python main.py
   ```

2. **Using the GUI:**

   - Enter your legal question in the provided text entry field.
   - Click the "Evaluate" button to process the question.
   - The answer will be displayed below the button in the format "The answer is (X)", where X is the index of the correct answer.

## Troubleshooting

- **No Display Found Error:** If you encounter a "No display found" error, ensure that `Xvfb` is installed and properly configured.
- **Unknown Question Response:** If the application returns "Unknown question," ensure that your question pertains to the Rule in Shelley's Case.

## Support

For additional support or to report issues, please contact our support team at support@chatdev.com. We are committed to providing comprehensive assistance to ensure your experience with the Legal Question Evaluator is seamless and productive.

Thank you for choosing the Legal Question Evaluator. We hope it serves as a valuable tool in your legal analysis endeavors.