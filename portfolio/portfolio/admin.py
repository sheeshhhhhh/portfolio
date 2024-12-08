from django.contrib import admin
from .models import Project, Skills, Education

# Admin configuration for Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'website_link', 'tech_stack')  # Fields to display in the list view
    search_fields = ('title', 'description', 'github_link', 'website_link', 'tech_stack')  # Fields to search
    list_filter = ('tech_stack',)  
    ordering = ('title',)  


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'knowledgeLevel', 'icon_display')  
    search_fields = ('name', 'icon', 'knowledgeLevel')  
    list_filter = ('knowledgeLevel',)  
    ordering = ('name',)  # Order by name

    def icon_display(self, obj):
        """Display the icon as an HTML image tag if it's a URL."""
        return f'<img src="{obj.icon}" style="width: 30px; height: 30px;" />' if obj.icon else "No Icon"
    icon_display.allow_tags = True  # Allow HTML tags in the display

class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description')  
    search_fields = ('name', 'description')  
    ordering = ('year',)  # Order by year


admin.site.register(Project, ProjectAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Education, EducationAdmin)
