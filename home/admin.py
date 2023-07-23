from django.contrib import admin
from django import forms
from home.models import Blog
from .models import Projects

# Register your models here.
class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Blog
        fields = "__all__"

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

class ProjectsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Projects
        fields = "__all__"

class ProjectsAdmin(admin.ModelAdmin):
    form = ProjectsAdminForm

admin.site.register(Blog, BlogAdmin)

admin.site.register(Projects, ProjectsAdmin)