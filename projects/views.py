# projects/views.py

from django.http import JsonResponse
from projects.models import Project
from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.core.mail import send_mail


def project_index(request):
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 2)
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


def contact_form(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')

        # Code to send email goes here
        send_mail(subject=subject, message=message, from_email=email, recipient_list=[
                  'juliusn411@gmail.com', 'njeruthelearner@gmail.com'])

        return redirect('home')
    else:
        return JsonResponse({'status': 'error'}, status=400)
