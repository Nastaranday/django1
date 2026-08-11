from django.contrib.auth.models import User
from product.models import Category, Product
from blogs.models import B_category, Employees,Blogs


def general_objects(request):
    context = {
        'employees_count' : Employees.objects.filter(status = True).count(),
        'users_count' : User.objects.all().count(),
        'products_count' : Product.objects.filter(status = True).count(),
        'blogs_count' : Blogs.objects.filter(status = True).count(),
        'p_category' : Category.objects.all(),
    }
    return context