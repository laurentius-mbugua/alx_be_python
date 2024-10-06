class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out=False

    def checked_out(self):
        self._is_checked_out=True

    def returned_book(self):
        self._is_checked_out=False

    def is_available(self):
        return not self._is_checked_out

class Library:
        def __init__(self):
            self.books = []

        def add_book(self, title, author):
            self.books.append(Book(title, author))

        def checked_out(self, title):
            for book in self.books:
                if book.checked_out():
                    book.checked_out()
                    print(f"Checked out '{title}'")
                    return True
                else:
                    print(f"Book '{title}' is not available or does not exist.")
                    return False


        def returned_books(self):
            for book in self.books:
                if book.returned_book():
                    book.returned_book()
                    print(f"Returned book '{book.title}'")
                    return True
                else:
                    print(f"Book '{book.title}' is not available or does not exist.")
                    return False

        def list_available_books(self):
            available_books = [book for book in self.books if book.is_available()]
            if not available_books:
                print("No books are currently available.")
            else:
                for book in available_books:
                    print(f"{book.title} by {book.author}")


