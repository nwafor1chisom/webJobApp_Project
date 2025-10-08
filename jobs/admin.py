from django.contrib import admin
from .models import JobPost

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'employer', 'location', 'category', 'deadline']
    list_filter = ['category', 'location']

