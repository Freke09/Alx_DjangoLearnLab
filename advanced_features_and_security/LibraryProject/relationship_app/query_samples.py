import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LIBRARYPROJECT.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        for book in books:
            return book.title
    except Author.DoesNotExist:
        return f"No author found with the name {author_name}"

def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            return f"{book.title} by {book.author.name}"
    except Library.DoesNotExist:
        return f"No library found with the name {library_name}"

def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except Librarian.DoesNotExist:
        return f"No librarian found for the library {library_name}"

