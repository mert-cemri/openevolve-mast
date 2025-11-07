# Max Fill User Manual

Welcome to the Max Fill software, a Python-based application designed to calculate the number of times buckets need to be lowered to empty all the wells in a grid. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it effectively.

## Introduction

The Max Fill software is a simple yet powerful tool that helps you determine the number of times you need to lower buckets to extract water from a grid of wells. Each well is represented by a row in a grid, and each '1' in a row represents a single unit of water. The software calculates the total number of water units and determines how many times the buckets need to be lowered based on their capacity.

## Quick Install

To use the Max Fill software, you need to have Python installed on your system. The software does not require any external dependencies, so the installation process is straightforward.

### Step 1: Install Python

If you haven't already, download and install Python from the official website: [python.org](https://www.python.org/). Follow the instructions provided for your operating system.

### Step 2: Clone the Repository

Clone the repository containing the Max Fill software to your local machine using the following command:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of the repository.

### Step 3: Navigate to the Project Directory

Navigate to the directory where the project files are located:

```bash
cd <project-directory>
```

Replace `<project-directory>` with the path to the cloned repository.

## How to Use

The Max Fill software is designed to be simple and easy to use. Follow these steps to calculate the number of times buckets need to be lowered:

### Step 1: Open the `main.py` File

Open the `main.py` file in a text editor or an integrated development environment (IDE) of your choice.

### Step 2: Define the Grid and Bucket Capacity

In the `main.py` file, define the grid of wells and the bucket capacity. For example:

```python
grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
capacity = 1
```

### Step 3: Call the `max_fill` Function

Call the `max_fill` function with the grid and capacity as arguments:

```python
result = max_fill(grid, capacity)
print("Number of times buckets need to be lowered:", result)
```

### Step 4: Run the Script

Run the `main.py` script using the following command:

```bash
python main.py
```

The output will display the number of times the buckets need to be lowered to empty all the wells.

## Conclusion

The Max Fill software is a simple yet effective tool for calculating the number of times buckets need to be lowered to extract water from a grid of wells. With its straightforward installation process and easy-to-use interface, you can quickly determine the required bucket lowerings for any given grid and bucket capacity. Enjoy using the Max Fill software!