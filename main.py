# main.py
# Entry point of the Spending Personality Analyser.
# Connects all modules and runs the main app loop.

from tracker  import add_expense, view_expenses, save_expenses, load_expenses
from analyser import run_analysis
from report   import generate_report


def main():
    print("==========================================")
    print("  Spending Personality Analyser")
    print("==========================================")

    expenses = load_expenses()
    print(f"  Loaded {len(expenses)} existing expense(s).")

    while True:
        print("\nWhat do you want to do?")
        print("  1. Add expense")
        print("  2. View all expenses")
        print("  3. Analyse my spending")
        print("  4. Quit")

        choice = input("\nEnter choice (1/2/3/4): ").strip()

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
            if len(expenses) == 0:
                print("\n  No expenses yet. Add some first!")
            else:
                grouped, percentages, personality = run_analysis(expenses)
                generate_report(expenses, grouped, percentages, personality)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print(f"  '{choice}' is not valid. Enter 1, 2, 3, or 4.")


main()