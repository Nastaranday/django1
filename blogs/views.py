from django.shortcuts import render
from .models import Blogs, Employees, Skills, B_category, Tags
# Create your views here.

def blog(request):
    blogs = Blogs.objects.filter(status = True)
    context = {
        'blogs' : blogs,
    }
    return render(request, 'blogs/blog.html', context = context)

def blogs_detail(request):
    d_blogs = Blogs.objects.filter(status = True)
    context = {
        'd_blogs' : d_blogs,
    }
    return render(request, 'blogs/blog-details.html', context = context)