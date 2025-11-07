'''
This file is the entry point of the Budget Tracker application.
'''
from budget_tracker import BudgetTracker
from dashboard import Dashboard
def main():
    budget_tracker = BudgetTracker()
    dashboard = Dashboard(budget_tracker)
    dashboard.run()
if __name__ == "__main__":
    main()