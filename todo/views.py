from asyncio import ProactorEventLoop, proactor_events
from django.shortcuts import render, redirect
from .models import emp
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import EmpRegistrationForm, ProjectForm
from .models import Project
from .forms import ProjectForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from .models import emp, Project

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = EmpRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other page after successful form submission
            return redirect('home')
    else:
        form = EmpRegistrationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Retrieve the user from the sign model using the provided username
        try:
            user = emp.objects.get(username=username)
        except emp.DoesNotExist:
            user = None

        if user is not None:
           
            if user.password == password:
              
                return redirect('project')  
            else:
                error_message = "Invalid password. Please try again."
        else:
            error_message = "Invalid username. Please try again."

        return render(request, 'login.html', {'error_message': error_message})

  
    return render(request, 'login.html')



def project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Redirect to a success page or project list
            return redirect('tasks')
        messages.success(request, 'Project submitted successfully!')
    else:
        form = ProjectForm()
    
    # If the form is not valid, render the form with errors
    return render(request, 'project.html', {'form': form})


def tasks(request):
    projects = Project.objects.all()
    return render(request, 'user.html', {'projects': projects})

def employes(request):
    emps = emp.objects.all()
    return render(request, 'employe.html', {'emps':emps})



def assign(request):
    emps = emp.objects.all()
    projects = Project.objects.all()
    if request.method == 'POST':
        employee_username = request.POST.get('employee')
        project_name = request.POST.get('project')
        email = request.POST.get('email')

        # Get the selected employee and project
        selected_employee = emp.objects.get(username=employee_username)
        selected_project = Project.objects.get(name=project_name)

        # Send email
        subject = f'Project Assigned: {selected_project.name}'
        message = f'Hello {selected_employee.username},\n\nYou have been assigned to project "{selected_project.name}".\n\nBest regards,\nYour Company'
        from_email = 'srttiwari4289@gmail.com'
        to_email = [email]

        send_mail(subject, message, from_email, to_email)

        # Optionally, you can redirect the user to a success page after sending the email
        
    return render(request, 'assign.html', {'emps': emps, 'projects': projects})

