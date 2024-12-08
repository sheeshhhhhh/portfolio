from django import forms

from . import models


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['image', 'title', 'description', 'github_link', 'website_link', 'tech_stack']

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': "block w-full mb-5 text-sm max-w-lg text-gray-900 border border-gray-300 cursor-pointer bg-gray-50 "}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'block p-2.5 h-[120px] w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500'}))
    github_link = forms.URLField(widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    website_link = forms.URLField(
        required=False,
        widget=forms.TextInput(attrs={ 'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    tech_stack = forms.CharField(widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))

class SkillsForm(forms.ModelForm):
    class Meta:
        model = models.Skills
        fields = ['name', 'icon', 'knowledgeLevel']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    icon = forms.URLField(widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    knowledgeLevel = forms.ChoiceField(choices=models.KnowledgeLevel.choices, widget=forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))

class EducationForm(forms.ModelForm):
    class Meta:
        model = models.Education
        fields = ['name', 'description', 'year']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'block p-2.5 h-[120px] w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500'}))
    year = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer',
        'pattern': r'^\d{4}-\d{4}$',  # Regex for the "YYYY-YYYY" format
        'title': 'Enter a valid year range in the format YYYY-YYYY'
    }))

