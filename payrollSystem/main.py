import payrollController as p

while True:
    print("\n 💵💵💵EMPLOYEE PAYROLL SYSTEM 💵💵💵")
    print("""
1. Add Employee
2. Remove Employee
3. Add Allowance
4. Add Deduction
5. Generate Pay Slip
6. Show All Employees
7. Exit
""")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            p.add_employee()
        case 2:
            p.remove_employee()
        case 3:
            p.add_allowance()
        case 4:
            p.add_deduction()
        case 5:
            p.calculate_payroll()
        case 6:
            p.show_all_employees()
        case 7:
            print("👋 Exiting Payroll System")
            break
        case _:
            print("❌ Invalid Choice")
