from django.urls import path
from .views import *

# base App urls

urlpatterns = [
    path('', homepage, name='homepage'),
    path('project1/', project1, name='project1'),
    path('project2/', project2, name='project2'),
    path('project3/', project3, name='project3'),
]
