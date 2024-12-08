from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from . import forms, models


def home(request):
    return render(request, 'home.html', { "navigation": "home" })

def projects(request):

    projects = models.Project.objects.all()
    return render(request, 'projects.html', { "navigation": "projects", "projects": projects })

def about(request):

    techStack = models.Skills.objects.all() 
    schools = models.Education.objects.all()

    return render(request, 'about.html', { "navigation": "about", "techStack": techStack, "schools": schools })


@staff_member_required
def Adminprojects(request):
    projects = models.Project.objects.all()
    projectForm = forms.ProjectForm()

    return render(request, 'owneradmin/projects.html', { "navigation": "projects", "projects": projects, 'form': projectForm })

@staff_member_required
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

@staff_member_required
def AddProject(request):
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            projects = models.Project.objects.all()
            return render(request, 'owneradmin/projects.html', { "navigation": "projects", "projects": projects,  'form': form, 'notValid': True})
        
    return redirect(Adminprojects)

@staff_member_required
def DeleteProject(request, pk):
    project = get_object_or_404(models.Project, pk=pk)
    if(not project):
        return redirect(Adminprojects)

    project.delete()
    return redirect(Adminprojects)


# skills
@staff_member_required
def AdminSkills(request):
    skills = models.Skills.objects.all()
    skillsForm = forms.SkillsForm()

    return render(request, 'owneradmin/skills.html', { "navigation": "skills", "skills": skills, "form": skillsForm })

@staff_member_required
def AddSkills(request):
    if request.method == 'POST':
        form = forms.SkillsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            skills = models.Skills.objects.all()
            return render(request, 'owneradmin/skills.html', { "navigation": "skills", "skills": skills,  'form': form, 'notValid': True})
        
    return redirect(AdminSkills)

@staff_member_required
def DeleteSkills(request, pk):
    skill = get_object_or_404(models.Skills, pk=pk)
    if(not skill):
        return redirect(AdminSkills)

    skill.delete()
    return redirect(AdminSkills)

@staff_member_required
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

@staff_member_required
def AdminEducation(request):
    schools = models.Education.objects.all()
    educationForm = forms.EducationForm()

    return render(request, 'owneradmin/education.html', { "navigation": "education", "schools": schools, 'form': educationForm })

@staff_member_required
def AddEducation(request):
    if request.method == 'POST':
        form = forms.EducationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            schools = models.Education.objects.all()
            return render(request, 'owneradmin/education.html', { "navigation": "education", "schools": schools,  'form': form, 'notValid': True})
        
    return redirect(AdminEducation)

@staff_member_required
def DeleteEducation(request, pk):
    school = get_object_or_404(models.Education, pk=pk)
    if(not school):
        return redirect(AdminEducation)

    school.delete()
    return redirect(AdminEducation)

@staff_member_required
def EditEducation(request, pk):
    school = get_object_or_404(models.Education, pk=pk)

    if request.method == 'POST':
        form = forms.EducationForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            return redirect(AdminEducation)
    else:
        form = forms.EducationForm(instance=school)
    
    return render(request, 'owneradmin/editeducation.html', { "form": form })