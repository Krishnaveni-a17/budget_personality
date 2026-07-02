# tracker.py

#this file handles everything like viewing ,
# adding,deleting the expenses



VALID_CATEGORIES = ["Food", "Transport", "Shopping", "Utilities", "Subscriptions"]


def get_amount():
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
    print("Valid categories:", VALID_CATEGORIES)
    while True:
        category = input("Enter category: ")
        if category in VALID_CATEGORIES:
            return category
        else:
            print(f"'{category}' is not valid. Choose from the list above.")


def get_note():
    note = input("Enter a short note (e.g. Swiggy, Ola, EB Bill): ")
    return note


def get_date():
    date = input("Enter date (YYYY-MM-DD), e.g. 2026-07-03: ")
    return date


def add_expense():
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

