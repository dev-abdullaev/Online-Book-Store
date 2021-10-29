from django.urls import path

from .views import (
    BookDeleteView,
    BookUpdateView,
    CategoryCreateView,
    CategoryDetailView,
    CategoryListView,
    IndexView,
    add_book,
    category_list,
    product_detail,
)

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("book-create/", add_book, name="book_create"),
    path("book-detail/<slug:slug>/", product_detail, name="book_detail"),
    path("book-update/<slug:slug>/", BookUpdateView.as_view(), name="book_update"),
    path("book-delete/<slug:slug>/", BookDeleteView.as_view(), name="book_delete"),
    path("category-list/", CategoryListView.as_view(), name="category_list"),
    path("category-create/", CategoryCreateView.as_view(), name="category_create"),
    path("category-detail/<slug:slug>/", CategoryDetailView.as_view(), name="category_detail"),
    path("shop/<slug:category_slug>/", category_list, name="category_list"),
]
