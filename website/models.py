from distutils.command.upload import upload
from django.db import models

class Files(models.Model):
    image = models.FileField(upload_to='project_images')

    def __str__(self):
        return self.image.name

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    overview = models.TextField()
    thumbnail = models.ImageField(upload_to="projects_thumb", blank=True, null=True)
    gallery = models.ManyToManyField(Files, related_name='projs')
    description = models.TextField()
    github = models.URLField()
    website = models.URLField(blank=True, null=True)
    front_end = models.ManyToManyField(Technology, related_name="front", blank=True)
    back_end = models.ManyToManyField(Technology, related_name='back', blank=True)


    def __str__(self):
        return self.name

