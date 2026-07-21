# main.py
# Entry point of the Spending Personality Analyser.
# Uses ExpenseTracker class to manage all expense operations.
# Connects tracker, analyser, and report modules.

from tracker  import ExpenseTracker
from analyser import run_analysis
from report   import generate_report


def main():

    print("==========================================")
    print("   Spending Personality Analyser")
    print("==========================================")

    # One object manages all expense data and operations
    tracker = ExpenseTracker()
    print(f"  Loaded {len(tracker.get_expenses())} existing expense(s).")

    while True:
        print("\n  What do you want to do?")
        print("  1. Add expense")
        print("  2. View all expenses")
        print("  3. Analyse my spending")
        print("  4. Quit")

        choice = input("\n  Enter choice (1/2/3/4): ").strip()

        if choice == "1":
            expense = tracker.add()
            print(f"\n  Saved: ₹{expense['amount']:.2f} for "
                  f"{expense['category']} ({expense['note']}) "
                  f"on {expense['date']}")

        elif choice == "2":
            tracker.view()

        elif choice == "3":
            expenses = tracker.get_expenses()
            if len(expenses) == 0:
                print("\n  No expenses yet. Add some first!")
            else:
                grouped, percentages, personality = run_analysis(expenses)
                generate_report(expenses, grouped, percentages, personality)

        elif choice == "4":
            print("\n  Goodbye!")
            break

        else:
            print(f"  '{choice}' is not valid. Enter 1, 2, 3, or 4.")


main()