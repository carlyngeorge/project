# main.py
from expense import Expense
from expense_manager import ExpenseManager

manager = ExpenseManager()

def menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            manager.add_expense(Expense(date, amount, category, description))
            print("Expense added!")
        elif choice == "2":
            manager.view_expenses()
        elif choice == "3":
            manager.view_expenses()
            index = int(input("Enter index to delete: ")) - 1
            manager.delete_expense(index)
        elif choice == "4":
            manager.category_summary()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
