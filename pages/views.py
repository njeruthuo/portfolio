# pages/views.py

import os

from django.conf import settings
from django.http import FileResponse

from django.shortcuts import render
from projects.models import Project

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage


def home(request):
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
    return render(request, "pages/home.html", {'projects': projects})


def open_cv(request):
    cv_path = os.path.join(settings.MEDIA_ROOT, 'cv/Django.pdf')
    return FileResponse(open(cv_path, 'rb'), content_type='application/pdf')
