#this will contain my functions

import Library as l
from datetime import datetime
               #keys
books = {}   # b_id 
members = {} # m_id 


def add_book():
    b_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    books[b_id] = l.Book(b_id, title, author)
    print("✅ Book Added Successfully")


def remove_book():
    b_id = int(input("Enter Book ID to remove: "))
    if b_id in books:
        del books[b_id]
        print("✅ Book Removed")
    else:
        print("❌ Book Not Found")


def check_availability():
    b_id = int(input("Enter Book ID: "))
    if b_id in books:
        if books[b_id].availability:
            print("✅ Book is Available")
        else:
            print("❌ Book is Issued")
    else:
        print("❌ Book Not Found")


def add_member():
    m_id = int(input("Enter Member ID: "))
    name = input("Enter Member Name: ")
    admission_date = datetime.now().strftime("%d-%m-%Y")

    members[m_id] = l.Member(m_id, name, admission_date)
    print("✅ Member Added Successfully")


def remove_member():
    m_id = int(input("Enter Member ID to remove: "))
    if m_id in members:
        del members[m_id]
        print("✅ Member Removed")
    else:
        print("❌ Member Not Found")


def issue_book():
    m_id = int(input("Enter Member ID: "))
    b_id = int(input("Enter Book ID: "))

    if m_id not in members:
        print("❌ Member Not Found")
        return

    if b_id not in books:
        print("❌ Book Not Found")
        return

    if not books[b_id].availability:
        print("❌ Book Already Issued")
        return

    books[b_id].availability = False
    members[m_id].issued_book = books[b_id].title
    print("✅ Book Issued Successfully")


def who_has_book():
    for m in members.values():
        if m.issued_book:
            print(f"{m.name} has issued '{m.issued_book}'")


def show_all_books():
    for b in books.values():
        status = "Available" if b.availability else "Issued"  # ternary opt syntax remember it other wise java ternary will not work
        print(f"{b.b_id} | {b.title} | {b.author} | {status}")


# what other can i add ?.. password login , member access etc           