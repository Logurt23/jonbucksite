from django.urls import path
from .views import *

# base App urls

urlpatterns = [
    path('', homepage, name='homepage'),
]
