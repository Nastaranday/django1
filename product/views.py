from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request, p_category=None):
    if p_category:
        products = Product.objects.filter(category__name = p_category)
    else:
        products = Product.objects.filter(status = True)
    context = {
        'products' : products,
    }
    return render(request, 'product/product.html', context = context)

def product_detail(request, id):
    p_details = Product.objects.get(id=id)
    context = {
        'p_details' : p_details,
    }
    return render(request, 'product/details.html', context=context)

def price(request):
    return render(request, 'product/pricing.html')

def comments(request):
    return render(request, 'product/comments.html')