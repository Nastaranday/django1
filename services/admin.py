from django.contrib import admin
from .models import Services, Features, S_category, Options, Property, Price, Attribute
# Register your models here.

admin.site.register(Services)
admin.site.register(Features)
admin.site.register(S_category)
admin.site.register(Options)
admin.site.register(Property)
admin.site.register(Price)
admin.site.register(Attribute)