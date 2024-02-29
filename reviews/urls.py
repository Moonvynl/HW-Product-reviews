from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('product-details/<int:pk>/', product_details, name='product-details'),
]