import Controller as c

print("🥳🥳 Welcome to Attendance System 🥳🥳")

while True:
     print("""
     1. Add new Student
     2. Take attendance
     3. Show attendance
     4. Exit
     """)
     choice = int(input("Enter your choice : "))
     match choice:
          case 1:
               c.add_student()
          case 2:
               c.take_attendance()
          case 3:
               c.show_attendance()
          case 4:
               print(" Exiting...")
               break
          case _:
               print("❌ Invalid choice")
