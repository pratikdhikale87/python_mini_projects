from models.Account import Account
from utils.BankExceptions import AccountNotFound

accounts = {}  # acc_no : Account object


def create_account():
    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Name: ")
    acc_type = input("Account Type (Savings/Current): ")
    balance = float(input("Initial Deposit: "))

    accounts[acc_no] = Account(acc_no, name, acc_type, balance)
    print("✅ Account Created Successfully")


def get_account(acc_no):
    if acc_no not in accounts:
        raise AccountNotFound("Account does not exist")
    return accounts[acc_no]


def deposit_money():
    acc_no = int(input("Account Number: "))
    amount = float(input("Amount: "))

    acc = get_account(acc_no)
    acc.deposit(amount)
    print("✅ Deposit Successful")


def withdraw_money():
    acc_no = int(input("Account Number: "))
    amount = float(input("Amount: "))

    acc = get_account(acc_no)
    acc.withdraw(amount)
    print("✅ Withdraw Successful")


def check_balance():
    acc_no = int(input("Account Number: "))
    acc = get_account(acc_no)
    print(f"💰 Balance: {acc.balance}")


def mini_statement():
    acc_no = int(input("Account Number: "))
    acc = get_account(acc_no)

    print("\n MINI STATEMENT")
    for txn in acc.mini_statement():
        print(txn)
