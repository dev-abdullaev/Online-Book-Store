from django import forms

from .models import Book, Category


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "category",
            "book_name",
            "author_name",
            "description",
            "cover",
            "price",
            "discount_price",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]

