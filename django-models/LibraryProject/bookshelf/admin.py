from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in admin list
    list_filter = ('author', 'publication_year')            # Sidebar filters
    search_fields = ('title', 'author')                     # Search box for title and author

admin.site.register(Book, BookAdmin)

