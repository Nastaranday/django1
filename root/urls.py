from django.urls import path 
from .views import home,contact_us,about

app_name = 'root'

urlpatterns = [
    path('', home, name = 'home'),
    path('contact_us', contact_us, name = 'contact'),
    path('about_us', about, name = 'about'),
]
