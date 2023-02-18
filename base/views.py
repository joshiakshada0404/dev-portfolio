from django.shortcuts import render , redirect
from .models import Project ,Skill
from .forms import  projectForm

# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')

    context = {'projects' : projects, 'skills': skills , 'detailedSkills': detailedSkills}
    
    return render(request,'base/home.html', context )


def projectPage(request, pk) :
    project = Project.objects.get(id=pk)
    context = { 'project' :project}
    return render(request, 'base/project.html', context ) 


def addProject(request):
    form = projectForm()

    if request.method == 'POST' :
        form = projectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context ={ 'form': form }
    return render(request, 'base/project_form.html',context)


def editProject(request ,pk):
    project = Project.objects.get(id= pk)
    form = projectForm(instance=project)    #pahele vala data pahele se dikha raha hoga 

    if request.method == 'POST' :
        form = projectForm(request.POST , request.FILES ,instance=project)  #instance se pata chalega that edit kis project ko karna hai 
        if form.is_valid():
            form.save()
            return redirect('home')

    context ={ 'form': form }
    return render(request, 'base/project_form.html',context)