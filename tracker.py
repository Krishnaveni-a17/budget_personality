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
        category=category.strip().capitalize()
        if category in VALID_CATEGORIES:
            return category
        else:
            print(f"'{category}' is not valid. Choose from the list above.")


def get_note():
    while True:
        note = input("Enter a short note (e.g. Swiggy, Ola, EB Bill): ")
        note =note.strip()
        if len(note)>0:
            return note
        else:
            print("Note cannot be empty. Please enter something.")


def get_date():
    while True:
        date = input("Enter date (YYYY-MM-DD), e.g. 2026-07-03: ")
        if len(date)==10 and date[4]=="-" and date[7]=='-':
            return date
        else:
            print(f"'{date}' is not valid.")


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

def view_expenses(expenses):
    print("\n========================================")
    print("         YOUR EXPENSES SO FAR")
    print("========================================")

    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    total = 0

    for i, expense in enumerate(expenses):
        print(f"\n  [{i + 1}] Date     : {expense['date']}")
        print(f"       Amount   : ₹{expense['amount']:.2f}")
        print(f"       Category : {expense['category']}")
        print(f"       Note     : {expense['note']}")
        total += expense['amount']

    print("\n----------------------------------------")
    print(f"  TOTAL SPENT  : ₹{total:.2f}")
    print(f"  TOTAL ENTRIES: {len(expenses)}")
    print("========================================\n")


