#This is the main.py
#this is the entry point of app
#It connects all files together


# main.py

from tracker import add_expense, view_expenses


def main():
    print("==========================================")
    print("  Welcome to Spending Personality Analyser")
    print("==========================================")

    expenses = []          # this is your notebook — starts empty every run

    while True:
        print("\nWhat do you want to do?")
        print("  1. Add expense")
        print("  2. View all expenses")
        print("  3. Quit")

        choice = input("\nEnter choice (1/2/3): ")

        if choice == "1":
            expense = add_expense()
            expenses.append(expense)
            print("Expense added successfully!")

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            print("Goodbye! See you tomorrow.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()