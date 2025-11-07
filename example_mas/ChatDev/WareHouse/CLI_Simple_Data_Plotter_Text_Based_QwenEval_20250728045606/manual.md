# CLI Data Plotter User Manual

## Overview

The CLI Data Plotter is a simple command-line application designed to read a list of numbers from a file or standard input and generate basic text-based bar charts and line graphs in the terminal. It also includes a graphical user interface (GUI) for users who prefer a more interactive experience.

## Main Features

- **Command-line Interface (CLI):** Accepts input from files or standard input and generates bar charts and line graphs.
- **Graphical User Interface (GUI):** Provides a user-friendly interface to load data and view plots.
- **Bar Charts:** Displays data as vertical bars, with the height of each bar representing the value.
- **Line Graphs:** Connects data points with lines, showing trends over the dataset.

## Installation

### Prerequisites

- Python 3.6 or higher
- `tkinter` library (usually included with Python)

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repo/cli-data-plotter.git
   cd cli-data-plotter
   ```

2. **Install Dependencies:**

   The project does not have external dependencies beyond Python's standard library. However, if you encounter any issues with `tkinter`, you can install it using your package manager:

   - **On Ubuntu:**

     ```bash
     sudo apt-get install python3-tk
     ```

   - **On macOS:**

     ```bash
     brew install python-tk@3.9
     ```

   - **On Windows:**

     `tkinter` is usually included with the Python installer. If not, you can download and install it from the official Python website.

## Usage

### Command-line Interface (CLI)

1. **Running the CLI:**

   ```bash
   python main.py
   ```

2. **Options:**

   - `-f, --file <filename>`: Specify the input file containing numbers.
   - `-g, --gui`: Launch the graphical user interface.

3. **Examples:**

   - **Plot data from a file:**

     ```bash
     python main.py -f data.txt
     ```

   - **Plot data from standard input:**

     ```bash
     echo -e "1.0\n2.0\n3.0\n4.0" | python main.py
     ```

   - **Launch the GUI:**

     ```bash
     python main.py -g
     ```

### Graphical User Interface (GUI)

1. **Launching the GUI:**

   ```bash
   python main.py -g
   ```

2. **Using the GUI:**

   - **Load Data:**
     - Click the "Load Data" button.
     - Select a text file containing numbers.
     - The data will be loaded and displayed in the text area.

   - **Plot Data:**
     - Click the "Plot Data" button.
     - The bar chart and line graph will be generated and displayed in the text area.

## Troubleshooting

- **File Format:**
  - Ensure that the input file contains only numeric values, one per line.
  - Non-numeric values will cause an error.

- **GUI Issues:**
  - If the GUI does not launch, ensure that `tkinter` is installed and properly configured.
  - Check for any error messages in the terminal.

## Contributing

We welcome contributions to the CLI Data Plotter project. If you have any ideas, bug fixes, or improvements, please feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/your-repo/cli-data-plotter).

## License

The CLI Data Plotter is open-source software licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This manual should provide a comprehensive guide for users to understand and use the CLI Data Plotter effectively. If you have any specific requirements or additional features to include, please let me know!