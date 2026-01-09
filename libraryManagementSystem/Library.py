# Library.py

class Book:
    # book will have b_id, title, author, availability
    def __init__(self, b_id, title, author):
        self.b_id = b_id
        self.title = title
        self.author = author
        self.availability = True


class Member:
    def __init__(self, m_id, name, admission_date):
        self.m_id = m_id
        self.name = name
        self.admission_date = admission_date
        self.issued_book = None
