from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def about(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/about.html', {'projects':projects})
# Create your views here.
