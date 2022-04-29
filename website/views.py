from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'website/index.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {'project': project}
    return render(request, 'website/project_details.html', context)
