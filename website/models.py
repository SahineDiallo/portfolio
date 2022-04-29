from distutils.command.upload import upload
from django.db import models

class Files(models.Model):
    image = models.ImageField(upload_to='project_images')


class Project(models.Model):
    name = models.CharField(max_length=100)
    overview = models.TextField()
    thumbnail = models.ForeignKey(Files, on_delete=models.CASCADE, related_name='proj')
    gallery = models.ManyToManyField(Files, related_name='projs')
    description = models.TextField()
    github = models.URLField()
    website = models.URLField(blank=True, null=True)

