from django.urls import path
from .views import product,product_detail,price,comments

app_name = 'product'

urlpatterns = [
    path('', product, name = 'products'),
    path('p_detail',product_detail),
    path('price',price, name = 'prices'),
]
