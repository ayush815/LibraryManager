class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("\t*" +book)
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or already issued to someone else. Please wait until the book is returned")
            return False
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithm", "Python", "Django", "Flask", "HTML"])
    student = student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ===== Welcome to central Library =====
        Please choose an option: 
        1. List all the books
        2. Request a book
        3. Add or return a book
        4. Exit the library
        '''
        print(welcomeMsg)
        a = input("Enter a choise: ")
        try:
            a = int(a)
            if a == 1:
                centralLibrary.displayAvailableBooks()
            elif a == 2:
                centralLibrary.borrowBook(student.requestBook())
            elif a == 3:
                centralLibrary.returnBook(student.returnBook())
            elif a == 4:
                print("Thanks for using Central Library. Have a great day!")
                exit()
            else:
                print("Invalid choice!")
        except Exception as e:
            print(f"You entered a {e}")
    
