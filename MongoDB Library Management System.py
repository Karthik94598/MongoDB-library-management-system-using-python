'''Scenario:
You are tasked with creating a simple library management system using MongoDB and Python. The system should allow you to:

task 1:- Insert new books into the library database.
task 2:- Retrieve all books in the library.
task 3:- Find books by a specific author.
task 4:- Update the availability status of a book.
task 5:- Delete books from the library database.'''

import pymongo
MyClient = pymongo.MongoClient("mongodb://localhost:27017")

lib = MyClient["library"] # creating database named library
books = lib["book stack"] # creating collection named book stack
# task 3 started
def find_author_book(Author_name):
    x =books.find_one({"Author": Author_name})
    if x:
        print("Details of the book based on the author:")
        print(x)
    else:
        print(f"No books found for author '{Author_name}'.")
# task 4 started
def availability_status(book,status):
    res=books.update_one({"Title": book},
                     {"$set":{"status":status}})
    if res.modified_count>0:
        x=books.find_one({"Title": book},{"_id":0,"Title":1,"status":1})
        print("The updated status of the book is", x)
    else:
         print(f"No books on the name of '{book}'.")
# task 4 started
#task 1 started
books.insert_one({"Title": "To Kill a Mockingbird" , "Author": "Harper Lee" , "Year": 1960})
books.insert_many([{"Title": "1984" , "Author": "George Orwell" , "Year": 1949} , {"Title": "Pride and Prejudice" , "Author": "Jane Austen" , "Year": 1813},
                   {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald","Year": 1925}, {"Title": "Moby Dick","Author": "Herman Melville","Year": 1851},
                   {"Title": "War and Peace","Author": "Leo Tolstoy","Year": 1869},{"Title": "The Catcher in the Rye" , "Author": "J.D. Salinger","Year": 1951},
                   {"Title": "The Hobbit","Author": "J.R.R. Tolkien","Year": 1937},{"Title": "Fahrenheit 451","Author": "Ray Bradbury","Year": 1953},
                   {"Title": "Jane Eyre","Author": "Charlotte Brontë","Year": 1847}])
# task 1 ended
# task 2 started
for i in books.find():
    print(i)
# task 2 ended
Author_name = str(input("Enter Author name: "))
find_author_book(Author_name)
# task 3 ended
book_tittle = str(input("Enter book tittle: "))
status = str(input("Enter status os the book available or not available: ")).strip().lower()
while True:
    if status == "available" or "not available":
        availability_status(book_tittle,status)
        break
    else:
        status = str(input("Enter status os the book available or not available: ")).strip().lower()
# task 4 ended
# task 5 started
books.delete_many({})
# task 5 ended