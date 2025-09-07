from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Library, Librarian

def list_books(request):
    books = Book.objects.select_related("author").all()
    context = {"books": books}
    return render(request, "relationship_app/book_list.html", context)