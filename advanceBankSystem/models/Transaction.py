from datetime import datetime

class Transaction:
    def __init__(self, t_type, amount, balance):
        self.t_type = t_type
        self.amount = amount
        self.balance = balance
        self.time = datetime.now()

    def __str__(self):
        return f"{self.time} | {self.t_type} | Amount: {self.amount} | Balance: {self.balance}"
