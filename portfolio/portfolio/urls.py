"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),

    path('adminprojects/', views.Adminprojects, name='Adminprojects'),    
    path('addproject/', views.AddProject, name='AddProject'),
    path('deleteproject/<int:pk>/', views.DeleteProject, name='DeleteProject'),
    path('editproject/<int:pk>/', views.EditProject, name='EditProject'),

    path('adminskills/', views.AdminSkills, name='AddSkills'),
    path('addskills/', views.AddSkills, name='AddSkills'),
    path('deleteskills/<int:pk>/', views.DeleteSkills, name='DeleteSkills'),
    path('editskills/<int:pk>/', views.EditSkills, name='EditSkills'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)