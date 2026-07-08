from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, 'blogs/blog.html')

def blogs_detail(request):
    return render(request, 'blogs/blog-details.html')