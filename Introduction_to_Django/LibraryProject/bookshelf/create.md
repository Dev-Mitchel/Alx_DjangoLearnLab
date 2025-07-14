from bookshelf.models import Book

book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
>>> #  Expected output: Book instance created successfully and saved to the database
# Output: <Book: 1984>