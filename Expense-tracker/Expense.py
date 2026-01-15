class Expense:
     def __init__(self,desc,spend_amount, date):
          self.desc = desc
          self.spend_amount = spend_amount
          self.date = date
          

     def __str__(self):
        return f"{self.date} | {self.desc} | ₹{self.spend_amount}"