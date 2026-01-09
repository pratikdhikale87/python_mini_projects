from controller.BankController import *
from utils.BankExceptions import AccountNotFound

while True:
    print("""
BANK ACCOUNT SIMULATOR
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Mini Statement
6. Exit
""")

    try:
        choice = int(input("Enter choice: "))

        match choice:
            case 1:
                create_account()
            case 2:
                deposit_money()
            case 3:
                withdraw_money()
            case 4:
                check_balance()
            case 5:
                mini_statement()
            case 6:
                print("👋 Thank you for banking with us")
                break
            case _:
                print("❌ Invalid choice")

    except AccountNotFound as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
