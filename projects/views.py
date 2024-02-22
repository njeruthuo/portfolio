# projects/views.py

from projects.models import Project
from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage, Page


def project_index(request):
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        projects = paginator.page(page_number)
    except (EmptyPage):
        projects = paginator.page(page_number)
    except (InvalidPage):
        projects = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        projects = paginator.page(1)

    return render(request, "projects/project_index.html", {
        "projects": projects
    })


def project_detail(request, title):
    project = get_object_or_404(Project, title=title)
    return render(request, "projects/project_detail.html", {
        "project": project
    })
