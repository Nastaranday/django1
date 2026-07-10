from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    products = Product.objects.filter(status = True)
    context = {
        'products' : products,
    }
    return render(request, 'product/product.html', context = context)

def product_detail(request):
    return render(request, 'product/details.html')

def price(request):
    return render(request, 'product/pricing.html')

def comments(request):
    return render(request, 'product/comments.html')