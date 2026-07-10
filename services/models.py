from django.db import models

# Create your models here.

class Options(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
    
class Features(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(blank=True)
    options = models.ManyToManyField(Options)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class S_category(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)

class Property(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Services(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='services', default='service.jpg')
    content = models.TextField(default='its really helpful for individuals')
    property = models.ManyToManyField(Property)
    s_category = models.ManyToManyField(S_category)
    PDF_file = models.FileField(upload_to='documents', blank=True)
    DOC_file = models.FileField(upload_to='documents', blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Attribute(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)

class Price(models.Model):
    name = models.CharField(max_length=100)
    fee = models.FloatField(default=100)
    attribute = models.ManyToManyField(Attribute)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)