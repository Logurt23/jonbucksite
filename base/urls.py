from django.urls import path
from .views import *

# base App urls

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about.html/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('projectlist/', projectlist, name='projectlist'),
    path('project1.html/', project1, name='project1'),
    path('project2.html/', project2, name='project2'),
    path('project3.html/', project3, name='project3'),
]
