from Contact import Contact

con = {}   # name (lowercase) : Contact object


def add_Contact():
     name = input("Enter name : ").lower()
     mob_no = input("Enter mobile no : ")
     tel_no = input("Enter telephone no : ")
     address = input("Enter address : ")

     try:
          con[name] = Contact(name, mob_no, tel_no, address)
          print("✅ Contact Added Successfully")
     except Exception as e:
          print(e)


def remove_Contact():
     name = input("Enter name : ").lower()

     if name in con:
          del con[name]
          print("🗑️🚮 Contact Deleted Successfully 🗑️🚮")
     else:
          print("❌ Contact Not Found")


def search_Contact():
     name = input("Enter name : ").lower()

     if name in con:
          c = con[name]
          print(f"Name : {c.name}")
          print(f"Mobile : {c.mob_no}")
          print(f"Telephone : {c.tel_no}")
          print(f"Address : {c.address}")
     else:
          print("❌ Contact Not Found")


def all_Contact():
     if not con:
          print(" No contacts available")
          return

     print("\n📒 All Contacts\n")
     for c in con.values():
          print(f"{c.name}, {c.mob_no}, {c.tel_no}, {c.address}")
