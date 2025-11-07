# Process Management CLI Tool

## Quick Overview

This tool is a Command Line Interface (CLI) application designed to help users find and kill processes by their name. It lists all matching processes and asks for confirmation before killing any of them.

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- `psutil` library

### Installing Dependencies

You can install the required dependencies using `pip`. Run the following command in your terminal:

```bash
pip install -r requirements.txt
```

This will install `psutil`, which is used to interact with system processes.

## 🚀 Usage

### Running the CLI Tool

To start the tool, navigate to the directory containing `main.py` and run:

```bash
python main.py
```

### Main Functions

1. **Search for Processes**

   - When you run the tool, it will prompt you to enter the name of the process you want to search for.
   - It will then list all processes that match the given name.

2. **Kill Processes**

   - After listing the matching processes, you will be prompted to enter the PID(s) of the processes you want to kill.
   - You can enter multiple PIDs separated by spaces or commas.
   - For each PID, the tool will ask for confirmation before killing the process.

3. **Exit**

   - You can type `q` at any point during the process selection to exit the tool.

## 📖 Example Workflow

1. **Start the Tool**

   ```bash
   python main.py
   ```

2. **Search for a Process**

   ```
   Enter process name to search: python
   ```

3. **View Matching Processes**

   ```
   Found processes:
   PID: 1234, Name: python
   PID: 5678, Name: python3
   ```

4. **Select Processes to Kill**

   ```
   Enter PID(s) to kill (separated by spaces or commas) (or 'q' to quit): 1234
   ```

5. **Confirm Killing a Process**

   ```
   Are you sure you want to kill process 1234? (y/n): y
   Process 1234 killed.
   ```

6. **Exit the Tool**

   ```
   Enter PID(s) to kill (separated by spaces or commas) (or 'q' to quit): q
   ```

## 🛠️ Troubleshooting

- **No Processes Found**

  If no processes are found, the tool will notify you:

  ```
  No processes found.
  ```

- **Invalid PID**

  If you enter an invalid PID, the tool will notify you:

  ```
  Invalid PID: abc
  ```

- **Process Does Not Exist**

  If you try to kill a process that does not exist, the tool will notify you:

  ```
  Process 9999 does not exist.
  ```

- **Error Killing Process**

  If there is an error killing a process, the tool will notify you with the error message:

  ```
  Error killing process 1234: [Error Message]
  ```

## 📜 License

This software is provided under the MIT License. For more details, see the `LICENSE` file.

## 🙋‍♂️ Support

For any issues or questions, please feel free to reach out to our support team at support@chatdev.com.

---

This manual should provide a comprehensive guide for users to understand and use the Process Management CLI Tool effectively.