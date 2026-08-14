from django.shortcuts import render
from django.db.models import Count
from .models import Blogs, Employees, Skills, B_category, Tags
# Create your views here.

def blog(request, **kwargs):
    if request.GET.get('search') is not None:
        blogs = Blogs.objects.filter(description_1_contains=request.GET.get('search'))
    elif kwargs.get('tags') is not None:
        blogs = Blogs.objects.filter(tags__name=kwargs.get('tags'))
    elif kwargs.get('b_category') is not None:
        blogs = Blogs.objects.filter(b_category__name=kwargs.get('b_category'))
    elif kwargs.get('employee') is not None:
        blogs = Blogs.objects.filter(employees__user__username=kwargs.get('employee'))
    elif kwargs.get('date') is not None:
        blogs = Blogs.objects.filter(schedule=kwargs.get('date'))
    else:
        blogs = Blogs.objects.filter(status = True)
    context = {
        'blogs' : blogs,
    }
    return render(request, 'blogs/blog.html', context = context)

def blogs_detail(request, id):
    blog = Blogs.objects.get(id = id)
    b_categorys = B_category.objects.annotate(
        blogs_count = Count('blogs')
        )
    tags = Tags.objects.all
    last_five_blogs = Blogs.objects.filter(status = True)[:5]
    context = {
        'blog' : blog,
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