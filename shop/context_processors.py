from .models import Category


def category_links(request):
    categories = Category.objects.all()
    return {"category_links": categories}
