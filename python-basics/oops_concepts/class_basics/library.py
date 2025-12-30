class Library:
    
    # Define Constructor for ths Class
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def get_all_books(self):
        for book in self.books:
            print(book.name)
        
        return self.books
            
    def find_top_rated_books(self):
        max_rating = 0
        top_rated_books = []
        
        for book in self.books:
            if book.rating > max_rating:
                top_rated_books.clear()
                top_rated_books.append(book)
                max_rating=book.rating
            elif book.rating == max_rating:
                top_rated_books.append(book)
        
        print(f"Number of Top Rated Books {len(top_rated_books)}")        
        return top_rated_books
        
    def __repr__(self):
        return f"Nem of Library: {self.name}, Address of the Library: {self.address}"