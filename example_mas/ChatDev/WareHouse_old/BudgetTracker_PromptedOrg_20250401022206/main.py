'''
Main executable file to demonstrate the functionality of the Budget Tracker with input validation.
'''
from budget_tracker import BudgetTracker
def main():
    tracker = BudgetTracker()
    # Adding expenses with validation
    try:
        tracker.add_expense(50, 'Food', 'Groceries')
        tracker.add_expense(20, 'Transport', 'Bus ticket')
        tracker.add_expense(100, 'Entertainment', 'Concert ticket')
    except ValueError as e:
        print(f"Error adding expense: {e}")
    # Adding savings with validation
    try:
        tracker.add_saving(500, 'Monthly salary')
        tracker.add_saving(200, 'Freelance project')
    except ValueError as e:
        print(f"Error adding saving: {e}")
    # Display total expenses
    total_expenses = tracker.get_total_expenses()
    print(f"Total Expenses: ${total_expenses:.2f}")
    # Display total savings
    total_savings = tracker.get_total_savings()
    print(f"Total Savings: ${total_savings:.2f}")
    # Display balance
    balance = tracker.get_balance()
    print(f"Balance (Savings - Expenses): ${balance:.2f}")
    # Display expenses by category
    expenses_by_category = tracker.get_expenses_by_category()
    print("Expenses by Category:")
    for category, amount in expenses_by_category.items():
        print(f"  {category}: ${amount:.2f}")
if __name__ == "__main__":
    main()