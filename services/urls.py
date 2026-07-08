from django.urls import path
from .views import services, services_detail

urlpatterns = [
    path('', services),
    path('s_detail', services_detail),
]