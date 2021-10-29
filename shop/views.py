from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, View

from .forms import BookModelForm, CategoryForm
from .models import Book, Category


class IndexView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "book/index.html"
    context_object_name = "books"


@login_required
def add_book(request):
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()

            return redirect("home")

    else:
        form = BookModelForm()

    return render(request, "book/book_create.html", {"form": form})


@login_required
def product_detail(request, slug):
    product = get_object_or_404(Book, slug=slug, in_stock=True)
    return render(request, "book/book_detail.html", {"product": product})


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "book/book_update.html"
    form_class = BookModelForm

    def get_success_url(self):
        return reverse_lazy("book_detail", kwargs={"slug": self.object.slug})


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "book/book_delete.html"
    success_url = reverse_lazy("home")


####------------------------------------------------------------------------------
####--------------------------------Category--------------------------------------
####------------------------------------------------------------------------------


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "category/list.html"
    context_object_name = "categories"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "category/create.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "category/detail.html"
    context_object_name = "category"

    def get_success_url(self):
        return reverse_lazy("category_detail", kwargs={"slug": self.object.slug})


@login_required
def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Book.objects.filter(category=category)
    return render(request, "category/category.html", {"category": category, "products": products})
