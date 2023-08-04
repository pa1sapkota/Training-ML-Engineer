'''
Implement a simple program to interact with
the library catalog system. Create a Python class Book to represent a single book with
attributes: Title, Author, ISBN, Genre, Availability (whether the book is available for
borrowing or not). 


Create another Python class LibraryCatalog to manage the
collection of books with following functionalities:



- Add books by storing each book objects (Hint: Create an empty list in constructor
and store book objects)

- get book details and get all books from the list of objects

Lets say, we need a book borrowing process (what books are borrowed and what books
are available for borrowing). Implement logics to integrate this requirement in the above
system. Design the classes with a clear focus on adhering to the Single Responsibility
Principle(SRP) which represents that "A module should be responsible to one, and
only one, actor."


'''


class Book: 
    """BOoks Class """
    def __init__(self, title , author , isbn , genre , availability = True ): 
        self.title = title 
        self.author = author 
        self.isbn = isbn 
        self.genre = genre 
        self.availability = availability
    
    def __str__(self): 
        print("-"*100)
        return f"Books Details :\n{self.title} \nAuthor: {self.author} \nisbn:{self.isbn} \ngenre: {self.genre} \nBook availability; {self.availability} "
    

class LibraryCatalog: 
    """Library Catalog """
    def __init__(self): 
        # Using Composition to add the books to the Catalog 
        self.books = []
    

    def add_books(self, book_obj): 
        # Add Books to the self.books 
        self.books.append(book_obj)
    
    def get_books_details(self): 
        """GEt the Details about the Available Books 
        """
        for book in self.books: 
            # if book.availability: #if book is available 
            print(book) 
    
    
    def available_books(self):
        print("The Following Books are available")
        for book in self.books: 
            if book.availability: 
                print(book)
    def borrow_books(self, book_name): 
        for book in self.books: 
            if book.title == book_name: 
                if book.availability: 
                    print(f"Books {book_name} is borrowed with isbn {book.isbn}")
                    book.availability = False 
                    # print(book.availability)
                    print("This is working ")
                    break 
                else : 
                    print(f"{book_name} is not Available")



        

b1 = Book("Harry Potter and the deadly Hollow", "JK Rolling", 1,"Fiction", True )
b2 = Book("Harry Potter and the Half Blood  Prince", "JK Rolling", 2,"Fiction", False )
b3 = Book("Harry Potter and the Prisioner of Azkaban ", "JK Rolling", 3,"Fiction", True )
b4 = Book("Harry Potter and the Sccorcers Stone", "JK Rolling", 4,"Fiction", True )
b5 = Book("Harry Potter and the Sccorcers Stone", "JK Rolling", 5,"Fiction", True )
b6 = Book("Harry Potter and the Sccorcers Stone", "JK Rolling", 6,"Fiction", True )

# print(b1)
# print(b2)
# print(b3)
# print(b4)


catalog = LibraryCatalog()
catalog.add_books(b1)
catalog.add_books(b2)
catalog.add_books(b3)
catalog.add_books(b4)
catalog.add_books(b5)
catalog.add_books(b6)


# catalog.get_books_details()
catalog.borrow_books("Harry Potter and the Sccorcers Stone")

catalog.get_books_details()
