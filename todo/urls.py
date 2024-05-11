from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('project/', views.project, name="project"),
    path('tasks/', views.tasks, name="tasks"),
    path('emp/', views.employes, name="emps"),
    path('assign/', views.assign, name="assign")
]