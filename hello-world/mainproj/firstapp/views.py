from django.shortcuts import render

from .models import FirstApp, Tag, Review

def projects(request):
    projects = FirstApp.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = FirstApp.objects.get(id = pk)
    mytags = Tag.objects.all()
    context = {'project': project, 'mytags': mytags}
    return render(request, 'projects/project.html', context)
