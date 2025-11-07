```markdown
# Dashboard Application

A simple Python-based dashboard application using Tkinter for GUI development.

## Overview

The Dashboard Application is designed to provide a simple interface for displaying and refreshing data. It is built using Python and Tkinter, a standard GUI toolkit in Python. The application is modular, consisting of several components that handle different aspects of the application, such as data management and custom widgets.

## Main Features

- **Dashboard Interface**: A user-friendly interface for displaying data.
- **Data Management**: Load and refresh data from a JSON file.
- **Custom Widgets**: Extendable widgets for custom functionality.
- **Headless Mode**: Detects if running in a headless environment and adjusts accordingly.

## Quick Install

### Prerequisites

- Python 3.x installed on your system.

### Installation Steps

1. **Clone the Repository**

   Clone the repository to your local machine using:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**

   This project does not require any external dependencies beyond the Python standard library. However, ensure you have Tkinter installed, which is included with most Python installations.

   ```bash
   # No additional installation needed for dependencies
   ```

## How to Use

1. **Run the Application**

   Navigate to the project directory and execute the main application script:

   ```bash
   python main.py
   ```

2. **Using the Dashboard**

   - **Custom Widget**: The application includes a custom widget that is displayed on the dashboard.
   - **Refresh Data**: Click the "Refresh Data" button to load and display the latest data from the JSON file.

3. **Data Handling**

   - The application loads data from a JSON file (`sample_data.json`) located in the project directory.
   - If the data file is not found or contains errors, default data will be used.

## Documentation

For more detailed information on the components and their functionalities, refer to the following:

- **Main Application**: `main.py` initializes and runs the application.
- **Dashboard**: `dashboard.py` handles the creation and management of the dashboard interface.
- **Data Management**: `data_handler.py` manages data operations such as loading and saving.
- **Custom Widgets**: `widgets.py` contains classes for custom widgets used in the application.

## Troubleshooting

- **No Display Found**: If running in a headless environment (e.g., server without GUI), the application will notify you and run in headless mode.
- **Data File Issues**: Ensure `sample_data.json` is present and correctly formatted. Default data will be used if issues are detected.

## Support

For further assistance, please contact our support team or refer to the documentation provided within the codebase.
```
