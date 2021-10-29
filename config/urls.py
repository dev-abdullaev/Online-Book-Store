from django import contrib
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),
    path("cart-summary/", include("basket.urls")),
    path("", include("payment.urls")),
    path("orders/", include("orders.urls")),
    path("users/", include("account.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
