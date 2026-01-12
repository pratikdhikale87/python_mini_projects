import Controller as c
print("🥳🥳 Welcome to Expense System 🥳🥳")

while True:
     print("""
1. Add new Expense     
2. Show all Expenses
3. Exit
""")
     choice = int(input("Enter your choice : "))
     match choice:
          case 1:
               c.add_Expense()
          case 2:
               c.show_all_Expense()
          case 3:
               print(" Exiting...")
               break
          case _:
               print("❌ Invalid choice")
