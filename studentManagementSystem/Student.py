class Student:

    # Insert record
    
    def insertRecord(self, roll_no, name, c_name, mob_no, address):
        with open("studentData.txt", "a") as f:
            record = f"{roll_no},{name},{c_name},{mob_no},{address}\n"
            f.write(record)
        print("✅✅ Record inserted successfully✅✅")

    # Read all records 
    def readRecords(self):
        try:
            with open("studentData.txt", "r") as f:
                data = f.read()
                if data.strip() == "":
                    print(" No records found")
                else:
                    print("\nRoll | Name | Class | Mobile | Address")
                    print("➡️➡️" * 25)
                    print(data)   #learn how to print the input by sep="" opt here 
                    #create a def print_function bhava
        except FileNotFoundError:
            print("❌ No data file found")

    # Read specific record
    def readSpecificRecord(self, roll_no):
        found = False
        with open("studentData.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == roll_no:
                    print("\n✅✅ Record Found ✅✅")
                    print("Roll No :", data[0])
                    print("Name    :", data[1])
                    print("Class   :", data[2])
                    print("Mobile  :", data[3])
                    print("Address :", data[4])
                    found = True
                    break
        if not found:
            print("❌ Record not found ❌")

    # Delete record
    def deleteRecord(self, roll_no):
        lines = []  #because we are getting string we don't need that
        found = False

        with open("studentData.txt", "r") as f:
            lines = f.readlines()
          #   print(lines)  # just for simple testing

        with open("studentData.txt", "w") as f:
            for line in lines:
                if line.startswith(roll_no + ","):
                    found = True
                else:
                    f.write(line)

        if found:
            print("✅ Record deleted successfully")
        else:
            print("❌ Record not found")

    # Update record
    def updateRecord(self, roll_no):
        lines = []
        found = False

        with open("studentData.txt", "r") as f:
            lines = f.readlines()

        print("""
               What do you want to update?
               1. Name
               2. Roll No
               3. Class Name
               4. Mobile Number
               5. Address
               6. Exit
               """)
        print("➡️➡️"*40)
        choice = input("Enter choice: ")

        with open("studentData.txt", "w") as f:
            for line in lines:
                data = line.strip().split(",")

                if data[0] == roll_no:
                    found = True

                    match choice:
                        case '1':
                            data[1] = input("Enter new name: ")
                        case '2':
                            data[0] = input("Enter new roll no: ")
                        case '3':
                            data[2] = input("Enter new class name: ")
                        case '4':
                            data[3] = input("Enter new mobile number: ")
                        case '5':
                            data[4] = input("Enter new address: ")
                        case '6':
                            print("Update cancelled")
                        case _:
                            print("Invalid choice")

                    f.write(",".join(data) + "\n")
                else:
                    f.write(line)

        if found:
            print("✅✅ Record updated successfully ✅✅")
        else:
            print("❌ Record not found ❌")
