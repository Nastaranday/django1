from django.urls import path
from .views import services, services_detail

app_name = 'services'

urlpatterns = [
    path('', services, name = 'service'),
    path('s_category/<str:s_category>', services, name='s_category'),
    path('s_detail/<int:id>', services_detail, name='s_details'),
]