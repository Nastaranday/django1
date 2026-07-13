from django.urls import path
from .views import blog, blogs_detail, teams

app_name = 'blogs'

urlpatterns = [
    path('', blog, name = 'blog'),
    path('b_details', blogs_detail),
    path('teams', teams, name = 'teams')
]


