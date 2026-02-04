class Library:
    def __init__(self, Book):
        self.Book = Book
        
class Book:
    def __init__(self, title, author, year, ISBN):
        self.title = title
        self.author = author
        self.year = year
        self.ISBN = ISBN

    def __str__(self):
        return f" '{self.title}' by {self.author} ({self.year}) - ISBN: {self.ISBN}"
    
    def __eq__(self, other):
        return self.ISBN == other.ISBN
            