import LibraryController as l

while True:
    print("\n📚📚📚 LIBRARY MANAGEMENT SYSTEM📚📚📚")
    print("""
1. Add New Book
2. Check Book Availability
3. Remove Book
4. Add New Member
5. Remove Member
6. Issue Book
7. Who Has Book
8. Show All Books
9. Exit
""")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            l.add_book()
        case 2:
            l.check_availability()
        case 3:
            l.remove_book()
        case 4:
            l.add_member()
        case 5:
            l.remove_member()
        case 6:
            l.issue_book()
        case 7:
            l.who_has_book()
        case 8:
            l.show_all_books()
        case 9:
            print("👋 Exiting Library System")
            break
        case _:
            print("❌ Invalid Choice")
