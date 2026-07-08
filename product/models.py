from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
    
class Product(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(default='this product is very useful for you')
    category = models.ManyToManyField(Category)
    image_1 = models.ImageField(upload_to='products', default='product1.jpg')
    image_2 = models.ImageField(upload_to='products', default='product2.jpg', blank=True)
    image_3 = models.ImageField(upload_to='products', default='product3.jpg', blank=True)
    image_4 = models.ImageField(upload_to='products', default='product4.jpg', blank=True)
    client = models.CharField(max_length=120)
    product_url = models.CharField(max_length=120)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)