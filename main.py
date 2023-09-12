# task 1.1 Make Class(Library) with attributes:
# booksList
# name of library
# lent books (name of user, book)
# task 1.2 Make method to display available Books.
# task 1.3 Make method for books lending.
# Don't forget to check if book isn't already lent
# task 1.4 Make method to add Book to library.
# task 1.5 Make method to return borrowed book.
# task 2.1 Make object(Harry) with attributes:
# booksList = ['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS']
# name of library = "CodeWithHarry"
# task 2.2 Make program run with those choices. (Don't forget the welcome message)
# Display Books
# Lend a Book
# Add a Book
# Return a Book
# task 2.3 Make program ends or continue.

class Library:
    def __init__(self, list_of_books, library_name):
        if type(list_of_books) == list:
            self.list_of_books = list_of_books
            self.libray_name = library_name
            self.lent_books = {}

    def display(self):
        for book in self.list_of_books:
            print(book, end=' -- ')

    def lend_book(self, book_name, username):
        if book_name in self.list_of_books:
            if book_name not in self.lent_books().keys():
                print('there\'s ur book')
                self.lent_books[book_name] = username
            else:
                print('this book is lent')
        else:
            print('this book is not found')

    def add_book(self, book_name):
        self.list_of_books.append(book_name)

    def return_book(self, book_name):
        del self.lent_books[book_name]


Harry = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter',
                 'C++ Basics', 'Algorithms by CLRS'], "CodeWithHarry")
while True:
    print(f'''\t {Harry.libray_name} \n Welcome to our library \n Your option is:  \n
        \t1-Display Books\n
         \t2-Lend a Book\n
          \t3-Add a Book\n
           \t4-Return a Book \n''')
    option = int(input('Enter your option: '))

    if option == 1:
        Harry.display()
    elif option == 2:
        username = input('Enter ur Username: ')
        book_name = input('Enter ur book_name: ')
        Harry.lend_book(book_name, username)
    elif option == 3:
        book_name = input('Enter ur book_name: ')
        Harry.add_book(book_name)
    elif option == 4:
        book_name = input('Enter ur book_name: ')
        Harry.return_book(book_name)
    else:
        print('Wrong option\n')

    choice = input('continue? (y/n): \n')
    if choice == 'n':
        print('Thank U :)')
        break
