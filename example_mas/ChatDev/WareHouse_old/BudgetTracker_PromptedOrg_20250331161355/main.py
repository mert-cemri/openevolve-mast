'''
Main entry point for the budget tracker application.
'''
from budget_tracker import BudgetTracker
from expense import Expense
from income import Income
def main():
    tracker = BudgetTracker()
    # Example usage
    tracker.add_income(Income(amount=5000, source="Salary", date="2023-10-01"))
    tracker.add_expense(Expense(amount=150, category="Groceries", date="2023-10-02"))
    tracker.add_expense(Expense(amount=200, category="Utilities", date="2023-10-03"))
    print("Total Income:", tracker.total_income())
    print("Total Expenses:", tracker.total_expenses())
    print("Savings:", tracker.calculate_savings())
    # Ensure the Excel file is saved and closed properly
    tracker.excel_handler.save_and_close()
if __name__ == "__main__":
    main()