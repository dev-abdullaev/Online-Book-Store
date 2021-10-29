from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField()

    class Meta:
        ordering = ["title"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50, unique=True)
    author_name = models.CharField(max_length=50)
    description = models.TextField()
    cover = models.ImageField(upload_to="book_cover/")
    added_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(max_length=250)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    objects = models.Manager()
    products = ProductManager()

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.book_name}"

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.book_name)
        super(Book, self).save(*args, **kwargs)
