from django.shortcuts import render
from django.http import HttpResponse
from django.views import view
from .models import Author, Book, Library, Librarian

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(view):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)
        return render(
            request,
            "relationship_app/library_detail.html",
            {"library": library}
        ))