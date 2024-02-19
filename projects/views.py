# projects/views.py

from projects.models import Project
from django.shortcuts import render, get_object_or_404


def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)


def project_detail(request, title):
    project = get_object_or_404(Project, title=title)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)
