# expense_manager.py
import json
import os
from expense import Expense

DATA_FILE = "../data/expenses.json"

class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                for item in data:
                    self.expenses.append(Expense(**item))

    def save_expenses(self):
        with open(DATA_FILE, "w") as f:
            json.dump([e.__dict__ for e in self.expenses], f, indent=4)

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for i, e in enumerate(self.expenses, 1):
            print(f"{i}. {e.date} | {e.amount} | {e.category} | {e.description}")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            self.save_expenses()
            print(f"Removed: {removed.description}")
        else:
            print("Invalid index!")

    def category_summary(self):
        summary = {}
        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount
        print("\nCategory Summary:")
        for cat, amt in summary.items():
            print(f"{cat}: {amt}")
