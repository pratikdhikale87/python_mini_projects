from models.Transaction import Transaction

class Account:
    DAILY_WITHDRAW_LIMIT = 50000

    def __init__(self, acc_no, name, acc_type, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
        self.transactions = []
        self.active = True
        self.withdraw_today = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")

        self.balance += amount
        self.transactions.append(Transaction("DEPOSIT", amount, self.balance))

    def withdraw(self, amount):
        if not self.active:
            raise ValueError("Account is blocked")

        if amount <= 0:
            raise ValueError("Invalid withdraw amount")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        if self.withdraw_today + amount > self.DAILY_WITHDRAW_LIMIT:
            raise ValueError("Daily withdraw limit exceeded")

        self.balance -= amount
        self.withdraw_today += amount
        self.transactions.append(Transaction("WITHDRAW", amount, self.balance))

    def mini_statement(self):
        return self.transactions[-5:]
