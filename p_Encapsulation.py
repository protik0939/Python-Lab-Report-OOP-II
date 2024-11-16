# Scenario: You are working on a library management system and need to create a
# LibraryBook class to manage details about each book in the library. To prevent unauthorized
# changes to critical information, you should use encapsulation principles, specifically by
# employing private and protected attributes and methods.
#---------------------------
# Question:
##########
# 1. Create a LibraryBook class with the following attributes and methods:
# ○ A private attribute ISBN that stores the book’s ISBN number, which should not
# be accessible directly or modified from outside the class.
# ○ A protected attribute title to store the book’s title, which can be accessible
# within subclasses but should not be modified directly from outside.
# ○ A protected method display_basic_info() that prints the title and author
# of the book, intended to be used by subclasses for detailed display.
# ○ A public method get_ISBN() that returns the book’s ISBN in a secure way
# (e.g., masked format).
# ○ A public method borrow_book(borrower_name) that:
# ■ Changes the book’s status to "borrowed".
# ■ Prints a message indicating the book has been borrowed by
# borrower_name.
##########
# 2. Create a subclass called DigitalLibraryBook that inherits from LibraryBook.
# This subclass should:
# ○ Use the protected display_basic_info() method to print the book’s basic
# info along with additional information specific to digital books (e.g., file format).
##########
# 3. Perform the following actions:
# ○ Create an instance of LibraryBook with a specific title, author, and ISBN.
# ○ Display the masked ISBN using get_ISBN().
# ○ Borrow the book using borrow_book().
# ○ Create an instance of DigitalLibraryBook and display the book’s basic and
# digital information using display_basic_info().
#---------------------------
# Answer:
#---------------------------




class LibraryBook:
    def __init__(self, title, author, ISBN):
        # Private attribute: ISBN (can't be accessed directly)
        self.__ISBN = ISBN
        
        # Protected attributes: title and author (can be accessed in subclasses)
        self._title = title
        self._author = author
        
        # Status of the book
        self._status = "available"

    # Public method to get the masked ISBN (for secure access)
    def get_ISBN(self):
        # Masking the ISBN for secure display
        return f"****-****-{self.__ISBN[-4:]}"
    
    # Public method to borrow the book
    def borrow_book(self, borrower_name):
        if self._status == "available":
            self._status = "borrowed"
            print(f"Book '{self._title}' has been borrowed by {borrower_name}.")
        else:
            print(f"Book '{self._title}' is already borrowed.")
    
    # Protected method to display basic information about the book (intended for subclasses)
    def _display_basic_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")

class DigitalLibraryBook(LibraryBook):
    def __init__(self, title, author, ISBN, file_format):
        # Inheriting from LibraryBook
        super().__init__(title, author, ISBN)
        
        # Additional attribute for digital books
        self._file_format = file_format

    # Using the protected method to display basic info and then adding specific info for digital books
    def display_basic_info(self):
        self._display_basic_info()  # Call to protected method from parent class
        print(f"File Format: {self._file_format}")

# Creating an instance of LibraryBook
book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")

# Displaying the masked ISBN
print("Masked ISBN:", book.get_ISBN())

# Borrowing the book
book.borrow_book("John Doe")

# Creating an instance of DigitalLibraryBook
digital_book = DigitalLibraryBook("The Digital Age", "John Smith", "1234567890123", "PDF")

# Displaying the book's basic and digital information
digital_book.display_basic_info()
