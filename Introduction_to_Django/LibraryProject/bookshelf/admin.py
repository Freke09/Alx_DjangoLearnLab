from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date')
    

admin.site.register(Book, BookAdmin)
# Register your models here.
