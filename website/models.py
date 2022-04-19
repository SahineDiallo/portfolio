from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class about(models.Model):
    description = models.TextField()
    image       = models.ImageField(upload_to='about')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField()
    role = models.CharField(max_length=100)


class technologies(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='technologies')
    description = models.TextField()

    def __str__(self):
        return self.name


class ProjectImages(models.Model):
    image = models.ImageField(upload_to='projects_images')
class Project(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField(ProjectImages)

