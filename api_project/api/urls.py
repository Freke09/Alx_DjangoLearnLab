from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListCreateAPIView, BookList, BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('book/create/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path("", include(router.urls)),
]