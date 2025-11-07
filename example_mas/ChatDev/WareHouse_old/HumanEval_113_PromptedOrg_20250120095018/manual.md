# Odd Count Software User Manual

Welcome to the Odd Count software! This application is designed to process a list of strings, where each string consists of only digits, and return a list of formatted strings indicating the number of odd digits in each input string.

## Main Functions of the Software

The primary function of this software is to analyze a list of strings containing digits and determine the number of odd digits in each string. The output is a list of strings formatted to replace placeholders with the count of odd digits.

### Function: `odd_count(lst)`

- **Input**: A list of strings, where each string consists of only digits.
- **Output**: A list of formatted strings, each indicating the number of odd digits in the corresponding input string.

#### Example Usage

```python
# Example input
input_list = ['1234567', '3', '11111111']

# Function call
output = odd_count(input_list)

# Expected output
# ["the number of odd elements 4n the str4ng 4 of the 4nput.",
#  "the number of odd elements 1n the str1ng 1 of the 1nput.",
#  "the number of odd elements 8n the str8ng 8 of the 8nput."]
```

## Installation Guide

### Prerequisites

- Python 3.x installed on your system.

### Installation Steps

1. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

2. **Set Up Virtual Environment (Optional but Recommended)**:
   - Create a virtual environment:
     ```bash
     python -m venv odd_count_env
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       odd_count_env\Scripts\activate
       ```
     - On macOS and Linux:
       ```bash
       source odd_count_env/bin/activate
       ```

3. **Install Dependencies**: There are no additional dependencies required for this software as per the `requirements.txt` file.

## How to Use

1. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

2. **Run the Script**: Execute the script using Python. You can test the function by calling it with sample input lists.

   ```bash
   python main.py
   ```

3. **Modify and Test**: You can modify the input list in the script to test with different data.

## Additional Information

- **Customization**: You can customize the function to handle different formats or additional logic as per your requirements.
- **Support**: For any issues or questions, please contact our support team.

Thank you for using the Odd Count software! We hope it meets your needs effectively.