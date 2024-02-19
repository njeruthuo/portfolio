# projects/models.py
from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:project_detail', args=[self.title])
