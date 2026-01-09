# what this system will have ? 
import Controller as c
print("📚📚📚🙏🙏🙏 Welcome to Contact Book System 🙏🙏🙏🙏📚📚📚")
while True:
     print("""
1.Enter new record.
2.Remove Contact.
3.Search Contact.
4.View All Contact
5.Exit.
""")

# match the cases 

     choice = int(input("Enter your choice :"))

     match choice:
          case 1:
               c.add_Contact()
          case 2:
               c.remove_Contact()
          case 3:
               c.search_Contact()
          case 4:
               c.all_Contact()
          case 5:
               exit()
          case _:
               print("❌ Invalid Choice...❌")