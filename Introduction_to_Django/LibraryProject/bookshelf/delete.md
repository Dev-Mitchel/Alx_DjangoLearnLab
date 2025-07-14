from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Try retrieving again
books = Book.objects.all()
print(books)

#  Output: <QuerySet []> — no books left