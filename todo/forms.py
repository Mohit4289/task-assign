from django import forms
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

class EmpRegistrationForm(forms.ModelForm):
    class Meta:
        model = emp
        fields = ['username','password']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'task_title', 'task_description', 'task_deadline', 'task_status']
"""
class ProjectRegistrationForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ['title','description','deadline','status']
"""