from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # could be many to one relation ships
    github_link = models.URLField()
    website_link = models.URLField()
    tech_stack = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# Project.objects.prefetch_related('images').all()
class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images')

    def __str__(self):
        return self.project.title

class Skills(models.Model):
    name = models.CharField(max_length=255)
    icon = models.TextField() # just a link
    knowledgeLevel = models.CharField(max_length=255) # Beginner - Intermediate - Advanced

    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
