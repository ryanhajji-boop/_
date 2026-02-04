# The main (parent) class for all items in the library
class StockItem:
    def __init__(self, title, date_acquired, on_loan=False):
        self.title = title
        self.date_acquired = date_acquired
        self.on_loan = on_loan

    def set_loan(self, loan_status):
        self.on_loan = loan_status

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Date Acquired: {self.date_acquired}")
        print(f"On Loan: {'Yes' if self.on_loan == True else 'No'}")


# A child class for books
class Book(StockItem):
    def __init__(self, title, author, isbn, date_acquired, on_loan=False):
        super().__init__(title, date_acquired, on_loan) # i want to 
        self.author = author
        self.isbn = isbn

    def display_details(self):
        super().display_details()  
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"ISBN: {self.isbn}")

class CD(StockItem):
    def __init__(self, title, artist, playing_time, date_acquired, on_loan=False):
        super().__init__(title, date_acquired, on_loan=False)
        self.artist = artist
        self.playing_time = playing_time

    def display_details(self):
        super().display_details()
        print(f"Artist: {self.artist}")
        print(f"Playing Time: {self.playing_time} minutes")


def tests():
    book1 = Book("1984", "George Orwell", "9780451524935", "2025-01-12")
    cd1 = CD("Abbey Road", "The Beatles", 47, "2024-10-01")
    
    items = [book1, cd1]
    for item in items:
        item.display_details()
    
tests()