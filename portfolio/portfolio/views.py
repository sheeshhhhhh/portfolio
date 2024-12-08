from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models


def home(request):
    return render(request, 'home.html', { "navigation": "home" })

# fix this later no more relation ships
def projects(request):

    projects = models.Project.objects.all()
    return render(request, 'projects.html', { "navigation": "projects", "projects": projects })

def about(request):

    techStack = models.Skills.objects.all() 
    schools = models.Education.objects.all()

    return render(request, 'about.html', { "navigation": "about", "techStack": techStack, "schools": schools })


# about projects
def Adminprojects(request):
    projects = models.Project.objects.all()
    projectForm = forms.ProjectForm()

    return render(request, 'owneradmin/projects.html', { "navigation": "projects", "projects": projects, 'form': projectForm })

def EditProject(request, pk):
    project = get_object_or_404(models.Project, pk=pk)

    if request.method == 'POST':
        form = forms.ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect(Adminprojects)
    else:
        form = forms.ProjectForm(instance=project)
    
    return render(request, 'owneradmin/editproject.html', { "form": form, 'Initialimage': project.image.url })

def AddProject(request):
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            projects = models.Project.objects.all()
            return render(request, 'owneradmin/projects.html', { "navigation": "projects", "projects": projects,  'form': form, 'notValid': True})
        
    return redirect(Adminprojects)

def DeleteProject(request, pk):
    project = get_object_or_404(models.Project, pk=pk)
    if(not project):
        return redirect(Adminprojects)

    project.delete()
    return redirect(Adminprojects)


# skills
def AdminSkills(request):
    skills = models.Skills.objects.all()
    skillsForm = forms.SkillsForm()

    return render(request, 'owneradmin/skills.html', { "navigation": "skills", "skills": skills, "form": skillsForm })

def AddSkills(request):
    if request.method == 'POST':
        form = forms.SkillsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            skills = models.Skills.objects.all()
            return render(request, 'owneradmin/skills.html', { "navigation": "skills", "skills": skills,  'form': form, 'notValid': True})
        
    return redirect(AdminSkills)

def DeleteSkills(request, pk):
    skill = get_object_or_404(models.Skills, pk=pk)
    if(not skill):
        return redirect(AdminSkills)

    skill.delete()
    return redirect(AdminSkills)

def EditSkills(request, pk):
    skill = get_object_or_404(models.Skills, pk=pk)

    if request.method == 'POST':
        form = forms.SkillsForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect(AdminSkills)
    else:
        form = forms.SkillsForm(instance=skill)
    
    return render(request, 'owneradmin/editskills.html', { "form": form })