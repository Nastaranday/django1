from django.urls import path
from .views import blog, blogs_detail, teams

app_name = 'blogs'

urlpatterns = [
    path('', blog, name = 'blog'),
    path('b_details/<int:id>', blogs_detail, name='b_details'),
    path('tags/<str:tags>', blog, name='tags'),
    path('employee/<str:employee>', blog, name='employee'),
    path('date/<str:date>', blog, name='date'),
    path('b_category/<str:b_category>', blog, name='b_category'),
    path('teams', teams, name = 'teams')
]


