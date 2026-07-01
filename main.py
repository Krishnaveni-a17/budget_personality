#This is the main.py
#this is the entry point of app
#It connects all files together


from tracker import add_expenses

def main():
    print("Welcome to Spending Personality Analyser")
    print("==========================================")

    expense=add_expenses()

    print("\n--- Expense Recorded ---")
    print(expense)


main()