from datetime import date
from Attend_Book import Details, Attendance   

students = []
attendance_records = []


def add_student():
    print("\n Add New Student")

    roll_no = int(input("Enter Roll No: "))
    s_name = input("Enter Student Name: ")
    address = input("Enter Address: ")
    mob_no = input("Enter Mobile No: ")
    class_name = input("Enter Class Name: ")

    student = Details(roll_no, s_name, address, mob_no, class_name)
    students.append(student)

    print("✅ Student added successfully\n")


def show_students():
    if not students:
        print("No students found")
        return

    print("\n Student List")
    print("-" * 40)
    for s in students:
        print(f"Roll: {s.roll_no} | Name: {s.s_name} | Class: {s.class_name}")
    print("-" * 40)


def take_attendance():
    if not students:
        print(" No students available. Add students first.")
        return

    today = date.today()
    day_name = today.strftime("%A")

    print(f"\n Attendance for {today} ({day_name})")

    for s in students:
        remark = input(f"Roll {s.roll_no} ({s.s_name}) [P/A]: ").upper()

        if remark not in ("P", "A"):
            remark = "A"

        record = Attendance(
            Date=str(today),
            Day=day_name,
            roll_no=s.roll_no,
            remark=remark
        )
        attendance_records.append(record)

    print("✅ Attendance completed\n")


def show_attendance():
    if not attendance_records:
        print(" No attendance records found")
        return

    print("\n Attendance Report")
    print("-" * 60)
    print("Date       | Day       | Roll No | Status")
    print("-" * 60)

    for a in attendance_records:
        status = "Present" if a.remark == "P" else "Absent"
        print(
            f"{a.Date:<10} | {a.Day:<9} | {a.roll_no:<7} | {status}"
        )

    print("-" * 60)
