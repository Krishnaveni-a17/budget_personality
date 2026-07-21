# tracker.py
# Handles all expense operations:
# input, validation, saving, loading, viewing.
# Contains both standalone functions and ExpenseTracker class.

import json
import os

VALID_CATEGORIES = ["Food", "Transport", "Shopping",
                    "Utilities", "Subscriptions"]


def save_expenses(expenses):

    os.makedirs("data", exist_ok=True)
    with open("data/expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)


def load_expenses():

    try:
        with open("data/expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def get_amount():

    while True:
        try:
            amount = input("Enter amount (₹): ")
            amount = float(amount)
            if amount <= 0:
                print("  Amount must be greater than zero. Try again.")
            else:
                return amount
        except ValueError:
            print("  Invalid amount! Enter a number like 450 or 99.50")


def get_category():

    print("  Valid categories:", VALID_CATEGORIES)
    while True:
        category = input("  Enter category: ").strip().capitalize()
        if category in VALID_CATEGORIES:
            return category
        else:
            print(f"  '{category}' is not valid. Choose from the list.")


def get_note():

    while True:
        note = input("  Enter a short note (e.g. Swiggy, Ola, EB Bill): ").strip()
        if len(note) > 0:
            return note
        else:
            print("  Note cannot be empty. Please enter something.")


def get_date():

    while True:
        date = input("  Enter date (YYYY-MM-DD), e.g. 2026-07-20: ")
        if len(date) == 10 and date[4] == "-" and date[7] == "-":
            return date
        else:
            print("  Invalid format. Use YYYY-MM-DD like 2026-07-20")


def add_expense():

    print("\n  --- Add New Expense ---")
    amount   = get_amount()
    category = get_category()
    note     = get_note()
    date     = get_date()

    return {
        "amount"  : amount,
        "category": category,
        "note"    : note,
        "date"    : date
    }


def view_expenses(expenses):

    print("\n  ========================================")
    print("           YOUR EXPENSES SO FAR")
    print("  ========================================")

    if len(expenses) == 0:
        print("  No expenses added yet.")
        return

    total = 0
    for i, expense in enumerate(expenses):
        print(f"\n  [{i+1}] Date     : {expense['date']}")
        print(f"       Amount   : ₹{expense['amount']:.2f}")
        print(f"       Category : {expense['category']}")
        print(f"       Note     : {expense['note']}")
        total += expense['amount']

    print("\n  ----------------------------------------")
    print(f"  TOTAL SPENT  : ₹{total:.2f}")
    print(f"  TOTAL ENTRIES: {len(expenses)}")
    print("  ========================================\n")


class ExpenseTracker:


    def __init__(self):

        self.expenses = load_expenses()

    def add(self):

        expense = add_expense()
        self.expenses.append(expense)
        save_expenses(self.expenses)
        return expense

    def view(self):

        view_expenses(self.expenses)

    def get_expenses(self):

        return self.expenses