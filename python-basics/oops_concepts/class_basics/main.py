from library import Library
from book import Book

libraray = Library("Valley Ranch", "1234 Vally View Ln")

#print(libraray)

java_book = Book("Java Basisc", "Katie", 1, 5)
libraray.add_book(java_book)

#print(java_book)

python_book = Book("Python Basics", "Natt", 2, 5)
libraray.add_book(python_book)

#print(python_book)

math_book = Book("Math Book", "Jhon", 3, 4)
libraray.add_book(math_book)

science_book = Book("Science Book", "Mohan", 3, 5)
libraray.add_book(science_book)

#print(math_book)

books = libraray.get_all_books()
print(f"Count of Books : {len(books)}")

top_rated_books = libraray.find_top_rated_books()
print(f"Number of top rated books: {len(top_rated_books)}")

# List Comprehension
[print(book) for book in top_rated_books]

# Print Top Rated Books info
