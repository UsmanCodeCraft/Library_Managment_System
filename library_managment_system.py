class Book:
    def __init__(self, title, author_name, isbn, copies):
        self.title = title
        self.author_name = author_name
        self.isbn = isbn
        self.copies = copies

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def search_book(self, title=None, author=None):
        results = self.books

        if title:
            filtered_results = []
            for book in results:
                if title.lower() in book.title.lower():
                    filtered_results.append(book)
            results = filtered_results

        if author:
            filtered_results = []
            for book in results:
                if author.lower() in book.author_name.lower():
                    filtered_results.append(book)
            results = filtered_results
        
        return results

    def borrow_book(self, isbn, user):
        for book in self.books:
            if book.isbn == isbn and book.copies > 0:
                book.copies -= 1
                if user not in self.borrowed_books:
                    self.borrowed_books[user] = []
                self.borrowed_books[user].append(book)
                return f"Book '{book.title}' borrowed by {user}"
        return "Book not available"

    def return_book(self, isbn, user):
        if user in self.borrowed_books:
            for book in self.borrowed_books[user]:
                if book.isbn == isbn:
                    book.copies += 1
                    self.borrowed_books[user].remove(book)
                    if not self.borrowed_books[user]:
                        del self.borrowed_books[user]
                    return f"Book '{book.title}' returned by {user}"
        return "Book not borrowed by user"
print("Welcome  to the Dangerous Library of the World ")

library = Library()
book1 = Book("1984", "George Orwell", "1234567890", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "1234567891", 2)
library.add_book(book1)
library.add_book(book2)

print(library.borrow_book("1234567890", "Alice"))
print(library.borrow_book("1234567890", "Bob"))
print(library.return_book("1234567890", "Alice"))

for book in library.search_book(author="George Orwell"):
    print(f"Found book: {book.title} by {book.author_name}")
