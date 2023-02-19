from django.shortcuts import render , redirect
from django.urls import reverse
from .models import Project ,Skill , Message
from .forms import  projectForm , MessageForm
from django.contrib import messages      # contact form fill krne ke bad message aaye user ko ki fill ho gaya hai 

# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')

    form = MessageForm()

    if request.method == 'POST' :
        form = MessageForm(request.POST)
        

        if form.is_valid():
            form.save()
            messages.success(request, 'Your message is Succesfully sent, will get in touch with you soon. Have a nice day.')
            return redirect('home')           
                     #isse resubmition vala problem solve ho ja raha aab refress karne me wapas resubmition nahi puchega 
    context = {'projects' : projects, 'skills': skills , 'detailedSkills': detailedSkills, 'form': form}
    
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


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')

    unreadCount = Message.objects.filter(is_read = False).count()

    context = { 'inbox': inbox , 'unreadCount':unreadCount}
    return render(request , 'base/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id = pk)
    message.is_read = True
    message.save()
    context = { 'message': message}
    return render(request , 'base/message.html', context)

