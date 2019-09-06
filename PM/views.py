from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Project

def index(request):
    """main page"""
    return render(request, 'PM/index.html')

def projects(request):
    """all projects page"""
    projects = Project.objects.order_by('date_add')
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
        from django.utils import timezone
        """
        temp_project = Project(name=request.POST.get('name'), author=request.POST.get('author'), year=request.POST.get('year'), month='month', day='day', state='ing')
        temp_project.save()

        return HttpResponseRedirect(reverse('PM:projects'))

    return render(request, 'PM/new_project.html')

def del_project(request, project_id):
    project = Project.objects.get(id=project_id)
    context ={'project':project}
    if request.method == 'POST':
        Project.objects.filter(id=project_id).delete()
        return HttpResponseRedirect(reverse('PM:projects'))
    
    return render(request, 'PM/del_project.html', context)

def renew_project(request, project_id):
    """Let you renew the project"""
    project = Project.objects.get(id=project_id)
    
    if request.method == 'POST':
    # Second request
        from django.utils import timezone
        temp_project = Project(name=request.POST.get('name'), author=request.POST.get('author'), year=request.POST.get('year'), month='month', day='day', state='ing', finished_time=timezone.now())
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
    project.state = 'finished'
    project.save()
    return HttpResponseRedirect(reverse('PM:projects'))
    #return render(request, 'PM/projects.html')

def search(request):
    search_content = request.GET.get('search_key')
    error_msg = ''

    if not search_content:
        error_msg = 'Please enter the key word'
        return render(request, 'PM/errors.html', {'error_msg':error_msg})

    projects = Project.objects.filter(name__icontains=search_content)
    return render(request, 'PM/search.html', {'error_msg': error_msg, 'projects': projects})
