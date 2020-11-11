from django.shortcuts import render
from datetime import date
from .forms import *

def success(request):
    return HttpResponse('successfully uploaded')

# Tailwinds CSS homepage
def homepage(request):
    return render(request, 'base/homepage.html', context={

    })

def about(request):
    return render(request, 'base/about.html',)

def contact(request):
    return render(request, 'base/contact.html',)

def projectlist(request):
    return render(request, 'base/projectlist.html',)

def project1(request):
    return render(request, 'base/project1.html',)

def project2(request):
    return render(request, 'base/project2.html',)

def project3(request):
    return render(request, 'base/project3.html',)
