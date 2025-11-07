# Calendar CLI Tool User Manual

## Overview

The Calendar CLI Tool is a command-line interface application designed to display a calendar for a given month and year. Users can input the month as a numeric value (1-12) or as a name (e.g., January, February), and the year as a numeric value. The tool will then output the calendar for the specified month and year.

## Main Functions

- **Input Handling**: Accepts user input for the month and year.
- **Validation**: Ensures the month and year inputs are valid.
- **Calendar Display**: Generates and displays the calendar for the specified month and year.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- `pip` (Python's package installer) should be available.

### Steps to Install

1. **Clone the Repository** (if not already done):
   ```bash
   git clone https://github.com/ChatDev/CalendarCLI.git
   cd CalendarCLI
   ```

2. **Install Dependencies**:
   This tool does not have any external dependencies beyond the Python standard library. However, if you encounter any issues, ensure your Python environment is correctly set up.

## Usage

### Running the Tool

1. **Navigate to the Project Directory**:
   ```bash
   cd path/to/CalendarCLI
   ```

2. **Run the Tool**:
   Use the following command to run the tool:
   ```bash
   python main.py <month> <year>
   ```
   Replace `<month>` with the desired month (either as a number or name) and `<year>` with the desired year.

   **Examples**:
   - Display the calendar for January 2023:
     ```bash
     python main.py January 2023
     ```
   - Display the calendar for March 2024:
     ```bash
     python main.py 3 2024
     ```

### Error Handling

- **Invalid Number of Arguments**: If you provide fewer or more than two arguments, the tool will display an error message and usage instructions.
- **Invalid Month**: If you provide an invalid month name or number, the tool will display an error message.
- **Invalid Year**: If you provide a non-numeric year, the tool will display an error message.

### Example Output

For the command `python main.py February 2023`, the output will be:
```
    February 2023
Mo Tu We Th Fr Sa Su
    1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28
```

## Additional Features

### Graphical User Interface (GUI)

In addition to the CLI, a graphical user interface (GUI) is provided for users who prefer a visual interface. To use the GUI, run the following command:
```bash
python calendar_gui.py
```

The GUI will open a window where you can enter the month and year, and then click the "Display Calendar" button to see the calendar.

## Conclusion

The Calendar CLI Tool is a simple yet powerful utility for displaying calendars. Whether you prefer using the command line or a graphical interface, this tool provides a convenient way to view any month's calendar for a given year. If you encounter any issues or have suggestions for improvement, please feel free to reach out to the development team.

---

This manual should provide users with a comprehensive understanding of how to use the Calendar CLI Tool, including installation, usage, and error handling.