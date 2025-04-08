import json
from datetime import datetime

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.borrower = None
        self.borrow_date = None

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}, Available: {'Yes' if self.borrower is None else 'Borrowed'}"

class Library:
    def __init__(self):
        self.books = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added successfully!")

    def search_book(self, query):
        results = [book for book in self.books if query in (book.title, book.author, book.isbn)]
        if results:
            for book in results:
                print(book)
        else:
            print("Book not found.")

    def borrow_book(self, isbn, borrower_name):
        for book in self.books:
            if book.isbn == isbn:
                if book.borrower is None:
                    book.borrower = borrower_name
                    book.borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Book '{book.title}' borrowed by {borrower_name} on {book.borrow_date}.")
                else:
                    print("This book is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.borrower is not None:
                    book.borrower = None
                    book.borrow_date = None
                    print(f"Book '{book.title}' returned successfully.")
                else:
                    print("This book was not borrowed.")
                return
        print("Book not found.")

    def view_all_books(self):
        if len(self.books) == 0:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(book)

    def save_data(self):
        data = []
        for book in self.books:
            book_data = {
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "isbn": book.isbn,
                "borrower": book.borrower,
                "borrow_date": book.borrow_date
            }
            data.append(book_data)
        with open("library_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open("library_data.json", "r") as file:
                data = json.load(file)
                for book_data in data:
                    book = Book(book_data["title"], book_data["author"], book_data["year"], book_data["isbn"])
                    book.borrower = book_data["borrower"]
                    book.borrow_date = book_data["borrow_date"]
                    self.books.append(book)
        except FileNotFoundError:
            print("No data file found. Starting with an empty library.")

def main():
    library = Library()

    while True:
        print("\nMenu:")
        print("1. Register Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View All Books")
        print("6. Save Data")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            year = input("Enter the publication year: ")
            isbn = input("Enter the book ISBN: ")
            book = Book(title, author, year, isbn)
            library.add_book(book)
        elif choice == 2:
            query = input("Enter the book title, author, or ISBN to search: ")
            library.search_book(query)
        elif choice == 3:
            isbn = input("Enter the ISBN of the book to borrow: ")
            borrower_name = input("Enter your name: ")
            library.borrow_book(isbn, borrower_name)
        elif choice == 4:
            isbn = input("Enter the ISBN of the book to return: ")
            library.return_book(isbn)
        elif choice == 5:
            library.view_all_books()
        elif choice == 6:
            library.save_data()
            print("Data saved successfully.")
        elif choice == 7:
            library.save_data()
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
