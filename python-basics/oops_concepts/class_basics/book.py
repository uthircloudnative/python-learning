class Book:
    
    def __init__(self, name, author, isbn, rating):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.rating = rating
        
    
    def __repr__(self):
        return f"Name: {self.name}, Author: {self.author}, Rating: {self.rating}"