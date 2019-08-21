from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Project

def index(request):
    """main page"""
    return render(request, 'PM/index.html')

def projects(request):
    """all projects page"""
    projects = Project.objects.order_by('finished_time')
    context = {'projects':projects}
    return render(request,'PM/projects.html',context)

def new_project(request):
    """add new project"""
    if request.method == 'POST':
        """
        temp_name = request.POST['name']
        temp_author = request.POST.get(author)
        temp_year = request.POST.get('year')
        temp_month = request.POST['month']
        temp_day = request.POST['day']
        """
        from django.utils import timezone
        temp_project = Project(name=request.POST.get('name'), author=request.POST.get('author'), year=request.POST.get('year'), month=request.POST.get('month'), day=request.POST.get('day'), finished_time=timezone.now())
        temp_project.save()

        return HttpResponseRedirect(reverse('PM:projects'))

    return render(request, 'PM/new_project.html')

def del_project(request, project_id):
    #ProjectID = request.project_id
    Project.objects.filter(id=project_id).delete()
    return HttpResponseRedirect(reverse('PM:projects'))

def renew_project(request, project_id):
    """Let you renew the project"""
    project = Project.objects.get(id=project_id)
    
    if request.method == 'POST':
    # Second request
        from django.utils import timezone
        temp_project = Project(name=request.POST.get('name'), author=request.POST.get('author'), year=request.POST.get('year'), month=request.POST.get('month'), day=request.POST.get('day'), finished_time=timezone.now())
        temp_project.save()

        Project.objects.filter(id=project_id).delete()
        return HttpResponseRedirect(reverse('PM:projects'))

    # First request, using instance project to pad the form
    context = {'project':project}
    return render(request, 'PM/renew_project.html', context)

def finished(request, project_id):
    project = Project.objects.get(id=project_id)
    from django.utils import timezone
    project.finished_time = timezone.now()
    project.save()
    return HttpResponseRedirect(reverse('PM:projects'))
    #return render(request, 'PM/projects.html')
