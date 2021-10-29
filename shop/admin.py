from django.contrib import admin

from .models import Book, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("book_name",)}
    list_display = ("book_name", "slug")


admin.site.register(Book, BookAdmin)
