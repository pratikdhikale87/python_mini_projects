import Employee as e

employees = {}  # emp_id : Employee object


def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    role = input("Enter Role: ")
    basic_salary = float(input("Enter Basic Salary: "))

    employees[emp_id] = e.Employee(emp_id, name, role, basic_salary)
    print("✅ Employee Added Successfully")


def remove_employee():
    emp_id = int(input("Enter Employee ID to remove: "))
    if emp_id in employees:
        del employees[emp_id]
        print("✅ Employee Removed")
    else:
        print("❌ Employee Not Found")


def add_allowance():
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in employees:
        amount = float(input("Enter Allowance Amount: "))
        employees[emp_id].allowance += amount
        print("✅ Allowance Added")
    else:
        print("❌ Employee Not Found")


def add_deduction():
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in employees:
        amount = float(input("Enter Deduction Amount: "))
        employees[emp_id].deduction += amount
        print("✅ Deduction Added")
    else:
        print("❌ Employee Not Found")


def calculate_payroll():
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in employees:
        emp = employees[emp_id]
        salary = emp.calculate_salary()
        print(f"""
💵💵 PAY SLIP💵💵
Employee : {emp.name}
Role     : {emp.role}
Basic    : {emp.basic_salary}
Allowance: {emp.allowance}
Expenses: {emp.deduction}
Total Pay  : {salary}
""")
    else:
        print("❌ Employee Not Found")


def show_all_employees():
    for emp in employees.values():
        print(f"{emp.emp_id} | {emp.name} | {emp.role} | {emp.calculate_salary()}")
