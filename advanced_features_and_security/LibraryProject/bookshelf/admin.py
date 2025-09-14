from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ['publication_year']
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'date_of_birth', 'is_staff')
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active")}
        ),
    )

    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()



admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
