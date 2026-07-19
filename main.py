# main.py
# Entry point of the Spending Personality Analyser.
# Connects all modules and runs the main app loop.

from tracker import add_expense, view_expenses, save_expenses, load_expenses


def main():
    print("==========================================")
    print("  Spending Personality Analyser")
    print("==========================================")

    # Load existing expenses from file when app starts.
    # First run: file doesn't exist yet → load_expenses() returns []
    # Every run after: loads saved expenses from data/expenses.json
    expenses = load_expenses()
    print(f"  Loaded {len(expenses)} existing expense(s).")

    while True:
        print("\nWhat do you want to do?")
        print("  1. Add expense")
        print("  2. View all expenses")
        print("  3. Quit")

        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == "1":
            expense = add_expense()
            expenses.append(expense)
            save_expenses(expenses)
            print(f"\n  Saved: ₹{expense['amount']:.2f} for "
                  f"{expense['category']} ({expense['note']}) "
                  f"on {expense['date']}")

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print(f"  '{choice}' is not valid. Enter 1, 2, or 3.")


main()