# projects/urls.py

from django.urls import path
from projects import views

app_name='projects'

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<str:title>/", views.project_detail, name="project_detail"),
]
