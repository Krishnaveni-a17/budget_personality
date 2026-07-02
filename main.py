#This is the main.py
#this is the entry point of app
#It connects all files together


from tracker import add_expense

def main():
    print("Welcome to Spending Personality Analyser")
    print("==========================================")

    expense=add_expense()

    print("\n--- Expense Recorded ---")
    print(expense)


main()