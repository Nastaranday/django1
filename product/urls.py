from django.urls import path
from .views import product,product_detail,price,comments

app_name = 'product'

urlpatterns = [
    path('', product, name = 'products'),
    path('category/<str:p_category>', product, name = 'p_category'),
    path('p_detail/<int:id>',product_detail, name='p_details'),
    path('price',price, name = 'prices'),
]
