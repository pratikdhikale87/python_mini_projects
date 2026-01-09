class AccountNotFound(Exception):
    def __init__(self, acc_no):
        self.acc_no = acc_no
        super().__init__(f"Account {acc_no} does not exist in the bank records")


class InsufficientBalance(Exception):
    def __init__(self, balance, amount):
        super().__init__(
            f"Insufficient balance | Available: {balance}, Requested: {amount}"
        )


class AccountBlocked(Exception):
    def __init__(self):
        super().__init__("Account is blocked. Please contact bank support")
