from django.urls import path
from .views import BookListCreateAPIView

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list')
    path('book/create/', BookListCreateAPIView.as_view(), name='book-list-create')
]