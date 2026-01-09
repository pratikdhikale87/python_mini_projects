class Employee:
    def __init__(self, emp_id, name, role, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.basic_salary = basic_salary
        self.allowance = 0
        self.deduction = 0

    def calculate_salary(self):
        return self.basic_salary + self.allowance - self.deduction
