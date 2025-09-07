from django.urls import path
from .views import list_books
from django.contrib.auth.vies import LoginView, LogoutView
from . import views
from .views import LibraryDetailView
# from .views import register_view
# from .views import login_view
# from .views import logout_view

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html") name='logout'),
]