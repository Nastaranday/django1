from django.shortcuts import render
from django.db.models import Count
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
    b_categorys = B_category.objects.annotate(
        blogs_count = Count('blogs')
        )
    tags = Tags.objects.all
    last_five_blogs = Blogs.objects.filter(status = True)[:5]
    context = {
        'd_blogs' : d_blogs,
        'last_five_blogs' : last_five_blogs,
        'b_categorys' : b_categorys,
        'tags' : tags,
    }
    return render(request, 'blogs/blog-details.html', context = context)

def teams(request):
    employees = Employees.objects.filter(status = True)
    context = {
        'employees' : employees
    }
    return render(request, 'blogs/team.html', context=context)