# Library Management System

class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print("Book issued successfully.")
        else:
            print("Book is not available.")

    def display_details(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Available:", self.available)


# Creating an object
b1 = Library("Python Programming", "Guido van Rossum")

b1.display_details()
b1.issue_book()
b1.display_details()


OUTPUT
Book Name: Python Programming
Author: Guido van Rossum
Available: True
Book issued successfully.
Book Name: Python Programming
Author: Guido van Rossum
Available: False
