from django.shortcuts import render

# Create your views here.

def product(request):
    return render(request, 'product/product.html')

def product_detail(request):
    return render(request, 'product/details.html')

def price(request):
    return render(request, 'product/pricing.html')

def comments(request):
    return render(request, 'product/comments.html')