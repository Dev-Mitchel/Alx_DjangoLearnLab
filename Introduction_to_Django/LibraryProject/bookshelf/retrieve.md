# Retrieve and display all attributes of the book you just created

from bookshelf.models import Book

# Retrieve the book (assuming it's the only one in the database or the first)
book = Book.objects.get(title="1984")

# Display its attributes
print("Title:", book.title)
print("Author:", book.author)
print("Published Date:", book.published_date)
print("ISBN:", book.isbn)

#  Expected Output:
# Title: 1984
# Author: George Orwell
# Published Year: 1949

