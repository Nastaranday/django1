from django.urls import path
from .views import blog, blogs_detail

urlpatterns = [
    path('', blog),
    path('b_details', blogs_detail),
]


