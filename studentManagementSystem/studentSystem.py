from Student import Student

print("🙏🙏🙏👏👏 Welcome to Student Management System 👏👏🙏🙏🙏")
stu = Student()  # Class chi pan practice hoil 

while True:
    print("⛔⛔"*25)
    print("""
1. Enter record
2. Update record
3. Delete record
4. Read all records
5. Read specific record
6. Exit
""")
    print("⛔⛔" * 25)
    try:
        choice = input("Enter choice: ")

        if choice == '1':
            roll_no = input("Enter roll number: ")
            name = input("Enter name: ")
            c_name = input("Enter class name: ")
            mob_no = input("Enter mobile number: ")
            address = input("Enter address: ")
            stu.insertRecord(roll_no, name, c_name, mob_no, address)

        elif choice == '2':
            roll_no = input("Enter roll number: ")
            stu.updateRecord(roll_no)

        elif choice == '3':
            roll_no = input("Enter roll number: ")
            stu.deleteRecord(roll_no)

        elif choice == '4':
            stu.readRecords()

        elif choice == '5':
            roll_no = input("Enter roll number: ")
            stu.readSpecificRecord(roll_no)

        elif choice == '6':
            print("👋 Bye bhava!")
            break

        else:
            print("❌ Invalid choice")

    except Exception as e:
        print("⚠️ Something went wrong:", e)
