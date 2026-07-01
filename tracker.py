#this file handles everything like viewing ,
# adding,deleting the expenses


def get_amount():
    amount=input("Enter Amount: ")
    return float(amount)

def get_category():
    category=input("Enter Category (Food,Transportation,Shopping,Subscriptions): ")
    return category

def get_note():
    note=input("Enter Note (Swiggy,Ola,EB Bill): ")
    return note

def get_date():
    date=input("Enter Time (YYYY-MM-DD)e.g. 2026-07-03:")
    return date


def add_expenses():
    print("\n--- Add New Expense ---")
    amount=get_amount()
    category=get_category()
    note=get_note()
    date=get_date()

    expenses={
        "amount":amount,
        "category":category,
        "note":note,
        "date":date

    }

    return expenses