from Expense import Expense

expenses = []

def add_Expense():
    desc = input("Enter description: ")
    amount = float(input("Enter amount spent: "))
    date = input("Enter date (DD-MM-YYYY): ")

    exp = Expense(desc, amount, date)
    expenses.append(exp)

    print("✅ Expense added successfully")


def show_all_Expense():
    if not expenses:
        print(" No expenses found")
        return

    print("\n All Expenses:")
    print("-" * 30)
    for exp in expenses:
        print(exp)
