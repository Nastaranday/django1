from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
      
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Employees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employess', default='employee.jpg')
    content = models.TextField(default='has good talent and knowledge')
    skills = models.ManyToManyField(Skills)
    twitter = models.CharField(max_length=120, blank=True)
    instagram = models.CharField(max_length=120, blank=True)
    facebook = models.CharField(max_length=120, blank=True)
    linkedin = models.CharField(max_length=120, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    class Mata:
        ordering = ('created_at',)

class B_category(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ('created_at',)
        
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)

class Blogs(models.Model):
    name = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='blogs', default='blog.jpg')
    bloger = models.ForeignKey(Employees, on_delete=models.CASCADE)
    b_category = models.ManyToManyField(B_category)
    tags = models.ManyToManyField(Tags)
    description_1 = models.TextField(default='In these days all people need to know')
    title_2 = models.CharField(max_length=120, blank=True, default='important')
    description_2 = models.TextField(default='this is really important', blank=True)
    title_3 = models.CharField(max_length=120, blank=True, default='focus') 
    description_3 = models.TextField(default='', blank=True)
    quoets = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    image_2 = models.ImageField(upload_to='blog', default='blog2.jp')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
    
