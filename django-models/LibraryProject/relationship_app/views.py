from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Library, Librarian

def list_books(request):
    books = Book.objects.all()
    book_list = ", ".join([book.title for book in books])
    return HttpResponse(f"Books: {book_list}")