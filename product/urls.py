from django.urls import path
from .views import product,product_detail,price,comments

urlpatterns = [
    path('product', product),
    
]
