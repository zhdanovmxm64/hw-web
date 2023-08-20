from django.urls import path
from catalog.views import index, contact, products, add_products
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('products/', products),
    path('add_products/', add_products),
]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)