# tracker.py
# This file handles everything related to
# adding, viewing, saving and loading expenses.

import json
import os

VALID_CATEGORIES = ["Food", "Transport", "Shopping", "Utilities", "Subscriptions"]


def save_expenses(expenses):
    """
    Saves the entire expenses list to data/expenses.json.
    Called every time a new expense is added.
    Why: so data survives after the app closes.
    """
    os.makedirs("data", exist_ok=True)
    with open("data/expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)


def load_expenses():
    """
    Loads expenses from data/expenses.json when app starts.
    Why: restores previously saved data automatically.
    Returns empty list if file doesn't exist yet (first run).
    """
    try:
        with open("data/expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def get_amount():
    """Asks user for amount. Validates it's a positive number."""
    while True:
        try:
            amount = input("Enter amount (₹): ")
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than zero. Try again.")
            else:
                return amount
        except ValueError:
            print("Invalid amount! Please enter a number like 450 or 99.50")


def get_category():
    """Asks user for category. Only accepts from VALID_CATEGORIES list."""
    print("Valid categories:", VALID_CATEGORIES)
    while True:
        category = input("Enter category: ").strip().capitalize()
        if category in VALID_CATEGORIES:
            return category
        else:
            print(f"'{category}' is not valid. Choose from the list above.")


def get_note():
    """Asks user for a short note. Cannot be empty."""
    while True:
        note = input("Enter a short note (e.g. Swiggy, Ola, EB Bill): ").strip()
        if len(note) > 0:
            return note
        else:
            print("Note cannot be empty. Please enter something.")


def get_date():
    """Asks user for date in YYYY-MM-DD format. Validates basic structure."""
    while True:
        date = input("Enter date (YYYY-MM-DD), e.g. 2026-07-20: ")
        if len(date) == 10 and date[4] == "-" and date[7] == "-":
            return date
        else:
            print("Invalid format. Please use YYYY-MM-DD like 2026-07-20")


def add_expense():
    """
    Collects all expense details from user.
    Returns a complete expense dictionary.
    """
    print("\n--- Add New Expense ---")
    amount   = get_amount()
    category = get_category()
    note     = get_note()
    date     = get_date()

    expense = {
        "amount"  : amount,
        "category": category,
        "note"    : note,
        "date"    : date
    }
    return expense


def view_expenses(expenses):
    """
    Displays all expenses in a formatted layout.
    Shows total spent and number of entries.
    """
    print("\n========================================")
    print("         YOUR EXPENSES SO FAR")
    print("========================================")

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

    print("\n----------------------------------------")
    print(f"  TOTAL SPENT  : ₹{total:.2f}")
    print(f"  TOTAL ENTRIES: {len(expenses)}")
    print("========================================\n")