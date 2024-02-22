# projects/urls.py

from django.urls import path
from projects import views

app_name='projects'

urlpatterns = [
    path("", views.contact_form, name="contact_form"),
    path("<str:title>/", views.project_detail, name="project_detail"),
]
