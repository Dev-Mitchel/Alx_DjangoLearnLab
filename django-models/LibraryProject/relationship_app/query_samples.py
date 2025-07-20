import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Import models
from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = 'Mitchel'
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"\nBooks by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"\nAuthor '{author_name}' not found.")

# 2. List all books in a library
library_id = 1  # change this to a real ID
try:
    library = Library.objects.get(id=library_id)
    books_in_library = library.books.all()
    print(f"\nBooks in library '{library.name}':")
    for book in books_in_library:
        print(f"- {book.title} by {book.author.name}")
except Library.DoesNotExist:
    print(f"\nLibrary with ID {library_id} not found.")

# 3. Retrieve the librarian for a library
try:
    librarian = library.librarian  # reverse OneToOneField access
    print(f"\nLibrarian for library '{library.name}': {librarian.name}")
except Exception as e:
    print(f"\nCould not retrieve librarian: {e}")

