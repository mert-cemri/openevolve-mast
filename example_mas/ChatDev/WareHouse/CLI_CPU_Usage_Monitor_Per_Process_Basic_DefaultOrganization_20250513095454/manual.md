# CLI CPU Usage Monitor

A command-line interface (CLI) application for monitoring CPU usage per process, similar to a simplified `top` command. This tool allows users to view CPU usage for all processes or focus on a specific process by providing its Process ID (PID).

## Main Functions

- **Monitor CPU Usage for All Processes:** Displays a list of all running processes along with their CPU usage percentage.
- **Focus on Specific Process:** Allows users to specify a PID to monitor CPU usage for a specific process.

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package manager)

### Quick Install

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   The primary dependency for this application is `psutil`, which is used for retrieving system and process information.

## How to Use

### Running the Application

1. **Monitor All Processes:**

   To start monitoring CPU usage for all processes, run the following command:

   ```bash
   python main.py
   ```

   This will display a list of all running processes along with their CPU usage percentage, updating every 2 seconds.

2. **Focus on a Specific Process:**

   To monitor CPU usage for a specific process, provide the PID using the `--pid` argument:

   ```bash
   python main.py --pid <PID>
   ```

   Replace `<PID>` with the actual Process ID you want to monitor. The application will display the CPU usage for the specified process, updating every 2 seconds.

### Example Usage

- To monitor all processes:

  ```bash
  python main.py
  ```

- To monitor a specific process with PID 1234:

  ```bash
  python main.py --pid 1234
  ```

### Notes

- The application updates the CPU usage information every 2 seconds.
- If a specified PID does not exist, the application will notify you with a message: "No process found with PID <PID>".

## Documentation

For further details on the implementation and usage of this application, please refer to the source code files:

- `main.py`: Contains the CLI logic and user interface.
- `process_monitor.py`: Contains the logic for retrieving CPU usage information using the `psutil` library.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the source code.