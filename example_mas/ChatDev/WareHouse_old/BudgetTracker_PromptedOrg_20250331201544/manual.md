manual.md

```
# Budget Tracker Application

Effortlessly monitor your expenses and savings with the Budget Tracker Application, a user-friendly Python-based dashboard designed to help you manage your finances effectively.

---

## 🚀 Key Features

- **Income Management**: Easily add and track your income sources.
- **Expense Tracking**: Record and categorize your expenses seamlessly.
- **Real-time Balance Calculation**: Instantly view your current financial balance.
- **Persistent Data Storage**: Your financial data is securely stored and retrieved automatically.
- **Intuitive Dashboard Interface**: User-friendly graphical interface for easy interaction.

---

## 📦 Installation and Setup

### Prerequisites

- Python 3.x installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Installation Steps

1. **Clone or Download the Application**

   Clone the repository or download the provided files to your local machine.

2. **Navigate to the Application Directory**

   Open your terminal or command prompt and navigate to the directory containing the application files.

   ```bash
   cd path/to/budget-tracker
   ```

3. **Install Dependencies**

   This application uses standard Python libraries and does not require external dependencies. However, ensure your Python environment is properly set up.

   ```bash
   # No external dependencies required
   ```

---

## 🖥️ Running the Application

### Using Python Directly

Run the application by executing the following command in your terminal:

```bash
python main.py
```

### Using the Provided Shell Script (Linux/MacOS)

Make sure the script has execution permissions:

```bash
chmod +x run.sh
```

Then execute the script:

```bash
./run.sh
```

---

## 🎯 How to Use the Budget Tracker

### Adding Income

1. Launch the application.
2. Enter your income details in the provided fields:
   - **Income Amount**: Enter the numeric value of your income.
   - **Income Source**: Specify the source of your income (e.g., Salary, Freelance).
   - **Income Description**: Provide additional details or notes (optional).
3. Click the **"Add Income"** button to save your entry.

### Adding Expenses

1. Enter your expense details in the provided fields:
   - **Expense Amount**: Enter the numeric value of your expense.
   - **Expense Category**: Specify the category of your expense (e.g., Groceries, Utilities).
   - **Expense Description**: Provide additional details or notes (optional).
2. Click the **"Add Expense"** button to save your entry.

### Viewing Financial Summary

- Click the **"Show Summary"** button to view a summary of your total income, total expenses, and current balance.

---

## ⚠️ Error Handling and Troubleshooting

- **Invalid Input**: If you enter a non-numeric or negative value, the application will display an error message. Please ensure all amounts entered are positive numeric values.
- **Data File Issues**: If the data file (`budget_data.json`) becomes corrupted, the application will automatically reset your data and notify you with a warning message.
- **Graphical Environment Required**: This application requires a graphical user interface (GUI). If you attempt to run it in a headless environment (e.g., a server without GUI), the application will exit gracefully with an error message.

---

## 📁 File Structure

```
budget-tracker/
├── budget_tracker.py   # Core logic for managing budget data
├── dashboard.py        # GUI dashboard for user interaction
├── main.py             # Entry point of the application
├── run.sh              # Shell script to launch the application
├── budget_data.json    # JSON file storing your budget data (auto-generated)
└── requirements.txt    # Dependencies information (no external dependencies)
```

---

## 📞 Support and Feedback

If you encounter any issues or have suggestions for improvement, please contact our support team or open an issue in the project's repository.

Thank you for choosing Budget Tracker Application to manage your finances effectively!

---