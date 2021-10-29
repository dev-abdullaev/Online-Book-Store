from django.urls import path

from . import views

urlpatterns = [
    path("", views.basket_summary, name="basket_summary"),
    path("add-books/", views.basket_add, name="basket_add"),
    path("delete-books/", views.basket_delete, name="basket_delete"),
    path("update-books/", views.basket_update, name="basket_update"),
]
