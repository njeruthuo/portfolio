# pages/views.py

from django.shortcuts import render
from projects.models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, "pages/home.html", {'projects': projects})
