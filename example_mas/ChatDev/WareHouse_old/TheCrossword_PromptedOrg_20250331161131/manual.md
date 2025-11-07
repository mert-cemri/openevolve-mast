# Crossword Puzzle Application

Welcome to the Crossword Puzzle Application! This user manual will guide you through the installation, main functions, and usage of the software.

## 📦 Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the directory where the project is cloned.

3. **Install Dependencies:**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have a `requirements.txt` file in the project directory listing all necessary dependencies.

## 🧩 Main Functions

The Crossword Puzzle Application provides the following main functions:

- **Display Grid:** Displays the current state of the crossword grid.
- **Enter Word:** Allows users to enter words into the grid by specifying the clue number and direction.
- **Validate Word:** Checks if the entered word matches the clue's answer and fits correctly in the grid.
- **Check Completion:** Confirms if all correct words are filled in the grid, indicating the puzzle is complete.

## 🎮 How to Use/Play

1. **Start the Application:**

   Run the application using the following command:

   ```bash
   python main.py
   ```

2. **Interact with the Application:**

   - You will be welcomed with a message and the initial empty grid will be displayed.
   - Enter the clue number when prompted.
   - Specify the direction (`across` or `down`) for the word placement.
   - Enter the word corresponding to the clue.

3. **Validation and Feedback:**

   - The application will validate the entered word and provide feedback.
   - If the word is entered successfully, the grid will update with the new word.
   - If the word entry fails, you will be prompted to try again.

4. **Completion:**

   - Continue entering words until the puzzle is complete.
   - Once all words are correctly filled, a congratulatory message will be displayed.

## 📚 Additional Information

For further assistance or inquiries, please contact our support team. We hope you enjoy solving the crossword puzzle with our application!