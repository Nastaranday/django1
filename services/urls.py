from django.urls import path
from .views import services, services_detail

app_name = 'services'

urlpatterns = [
    path('', services, name = 'service'),
    path('s_detail', services_detail),
]